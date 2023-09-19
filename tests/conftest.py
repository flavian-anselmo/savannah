from fastapi.testclient import TestClient
from app.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config.config import settings
from app.database.database import get_db
from app.database.database import Base
import pytest
from app.oauth import oauth2
from app.models import models

SQLALCHEMY_DATABASE_URL =  f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_host}/{settings.database_name}-db-testing'

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
        "customer_id": 1,
        "customer_name": "test_user",
        "phone_no": "+254798071510",
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

@pytest.fixture
def create_a_test_item(client,session):
    item_data =  {
        'item_id':1,
        'item_name':'test_item',
        'item_stock':9,
        'price':50.0
    }
    res = client.post(
        '/items',
        json=item_data
    )
    assert res.status_code == 201

@pytest.fixture
def token(create_test_user):
    return oauth2.create_access_token(
        payload={
            "customer_id": create_test_user['customer_id']
        }
    )
@pytest.fixture
def authorized_client(client, token):
    client.headers ={
        **client.headers,
        "Authorization":f"Bearer {token}"
    }
    return client


@pytest.fixture 
def create_multiple_test_items(create_test_user, session):
    item_data = [
        {
            'item_id':2,
            'item_name':'test_item_2',
            'item_stock':12,
            'price':56.0
        },
        {
            'item_id':3,
            'item_name':'test_item_3',
            'item_stock':10,
            'price':55.0
        }
    ]
    def create_items_model(item):
        return models.Items(**item)
        
    items_map = map(create_items_model, item_data)
    items = list(items_map)
    session.add_all(items)
    session.commit()
    items = session.query(models.Items).all()
    return items 

@pytest.fixture
def create_multiple_orders(create_test_user, create_multiple_test_items, session):
    order_data = [
        {
            'customer_id':1,
            'quantity':2,
            'item_id':2,
        },
        {    'customer_id':1,
            'quantity':1,
            'item_id':3
        }
    ]
    def create_order_model(order):
        return models.Orders(**order)
    order_map = map(create_order_model, order_data)
    orders = list(order_map)
    session.add_all(orders)
    session.commit()
    orders = session.query(models.Orders).all()
    return orders 
