from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.schemas.person import PersonaVerificarRequest, PersonaVerificarResponse
from app.services.person_service import PersonaService

router = APIRouter()
VALID_TOKEN = "mi_token_valido"

security = HTTPBearer()


def verificar_jwt(
        credentials: HTTPAuthorizationCredentials = Depends(security)
        ):
    token = credentials.credentials
    if token != VALID_TOKEN:
        raise HTTPException(status_code=401, detail="Token inválido")
    return True


@router.post("/verificar", response_model=PersonaVerificarResponse)
def verificar(
    request: PersonaVerificarRequest,
    auth: bool = Depends(verificar_jwt)
):
    """
    Verifica si una persona está en la lista negra.
    """
    service = PersonaService()
    try:
        encontrado = service.verify_person(request.nombre_completo)
        return {"encontrado": encontrado}
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Error al conectar con la base de datos"
            )
