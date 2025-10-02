from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PersonaBloqueada(Base):
    __tablename__ = "personas_bloqueadas"

    id = Column(Integer, primary_key=True, index=True)
    nombre_completo = Column(String, unique=True, nullable=False)
