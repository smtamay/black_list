from app.db.db import SessionLocal, engine
from app.models.person import PersonaBloqueada, Base

Base.metadata.create_all(bind=engine)

nombres_bloqueados = [
    "Juan Pérez González",
    "María López Hernández",
    "Carlos Sánchez Torres",
    "Ana Martínez Ruiz",
    "Luis Gómez Díaz",
    "Laura Fernández Morales",
    "Pedro Jiménez Castillo",
    "Sofía Romero García",
    "José Ramírez Ortega",
    "Marta Cruz Navarro"
]

db = SessionLocal()
for nombre in nombres_bloqueados:
    if not db.query(PersonaBloqueada).filter_by(nombre_completo=nombre).first():
        db.add(PersonaBloqueada(nombre_completo=nombre))
db.commit()
db.close()
