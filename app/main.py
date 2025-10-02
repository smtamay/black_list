from fastapi import FastAPI
from app.routes.person_routes import router as person_routers
from app.models.person import Base
from app.db.db import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Lista Negra", version="1.0")

app.include_router(person_routers)
