from fastapi.testclient import TestClient
from app.main import app
import pytest

from app.services.person_service import PersonaService

VALID_TOKEN = "mi_token_valido"
INVALID_TOKEN = "token_invalido"

client = TestClient(app)


class TestVerificarPersona:

    @pytest.fixture(autouse=True)
    def setup(self, monkeypatch):
        self.monkeypatch = monkeypatch

    def test_persona_encontrada(self):
        self.monkeypatch.setattr(
            PersonaService, "verify_person",
            lambda self, x: True
            )

        response = client.post(
            "/verificar",
            json={"nombre_completo": "Sandra Tamay"},
            headers={"Authorization": f"Bearer {VALID_TOKEN}"}
        )

        assert response.status_code == 200
        assert response.json() == {"encontrado": True}

    def test_persona_no_encontrada(self):
        self.monkeypatch.setattr(
            PersonaService, "verify_person",
            lambda self, x: False
            )

        response = client.post(
            "/verificar",
            json={"nombre_completo": "Juan Perez"},
            headers={"Authorization": f"Bearer {VALID_TOKEN}"}
        )

        assert response.status_code == 200
        assert response.json() == {"encontrado": False}

    def test_token_invalido(self):
        response = client.post(
            "/verificar",
            json={"nombre_completo": "Sandra Tamay"},
            headers={"Authorization": f"Bearer {INVALID_TOKEN}"}
        )

        assert response.status_code == 401
        assert response.json() == {"detail": "Token inválido"}

    def test_sin_token(self):
        response = client.post(
            "/verificar",
            json={"nombre_completo": "Sandra Tamay"}
        )
        assert response.status_code == 403

    def test_body_invalido(self):
        response = client.post(
            "/verificar",
            json={"nombre": "Sandra Tamay"},  # campo incorrecto
            headers={"Authorization": f"Bearer {VALID_TOKEN}"}
        )
        assert response.status_code == 422
