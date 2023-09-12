from fastapi import status
from app.main import app






def test_read_root(client):
    response = client.get('/healthcheck')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        'message': f'Health Check {app.version}'
    }

