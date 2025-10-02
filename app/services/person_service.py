from app.db.db import SessionLocal
from app.models.person import PersonaBloqueada


class PersonaService:
    def __init__(self):
        self.db = SessionLocal()

    def verify_person(self, nombre_completo: str) -> bool:
        try:
            persona = self.db.query(PersonaBloqueada).filter(
                PersonaBloqueada.nombre_completo == nombre_completo
            ).first()
            return persona is not None
        except Exception as e:
            raise e
        finally:
            self.db.close()
