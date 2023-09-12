from fastapi.testclient import TestClient
from app.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config.config import settings
from app.database.database import get_db
from app.database.database import Base
import pytest

SQLALCHEMY_DATABASE_URL =  f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_host}/{settings.database_name}-testing-db'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db 

    finally:
        db.close() 



@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session

        finally:
            session.close() 
    # override the db dependecy to create another db testing session  
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(
        app=app
    )

@pytest.fixture
def create_test_user(client):
    user_data = {
        "customer_name": "test_user",
        "phone_no": "+254798071520",
        "password": "12345678"
    }
    res = client.post(
        '/auth/sign-up',
        json=user_data
    )
    assert res.status_code == 201
    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user