from fastapi.testclient import TestClient
from app.main import app

test_client = TestClient(
    app=app
)

def test_healthchecker():
    response = test_client.get('/healthcheck')
    assert response.status_code ==200
    assert response.json() == {
        'message': f'Health Check {app.version}'
    }
