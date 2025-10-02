from pydantic import BaseModel


class PersonaVerificarRequest(BaseModel):
    nombre_completo: str


class PersonaVerificarResponse(BaseModel):
    encontrado: bool
