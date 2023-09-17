from fastapi import status
from app.schema import schema
import pytest


def test_sign_in_endpoint_for_missing_credentials(client):
    res = client.post(
        '/auth/sign-in'
    )
    assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY



def test_sign_in_endpoint_without_user_in_db(client):
    res = client.post(
        '/auth/sign-in',
        data={
            'username':'anselmo',
            'password':'string'
        }
    )
    assert res.status_code == status.HTTP_404_NOT_FOUND

def test_sign_up_endpoint(client):
    response = client.post(
        '/auth/sign-up', 
        json={
            "customer_name": "test_user",
            "phone_no": "+254798071520",
            "password": "12345678"
        }
    )
    new_user = schema.CustomerResponse(
        **response.json()
    )
    assert new_user.customer_name == 'test_user'
    assert new_user.phone_no == '+254798071520'
    assert response.status_code == status.HTTP_201_CREATED

def test_sign_in_endpoint(client, create_test_user):
    res = client.post(
        '/auth/sign-in',
        data = {
            'username':create_test_user['customer_name'],
            'password':create_test_user['password']
        }
    )
    print(res.json())    
    assert res.status_code == status.HTTP_200_OK

def test_sign_in_user_that_does_not_exist(client, create_test_user):
    res = client.post(
        '/auth/sign-in',
        data = {
            'username':'k',
            'password':'1234567'
        }
    )
    print(res.json())    
    assert res.status_code == status.HTTP_404_NOT_FOUND
