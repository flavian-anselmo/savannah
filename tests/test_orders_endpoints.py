from fastapi import status
from app.schema import schema
import pytest


@pytest.mark.skip(reason='avoid sending messages using my trial twilio account')
def test_make_orders_endpoint(authorized_client,create_multiple_test_items, create_multiple_orders):
    res = authorized_client.post(
        '/orders/2',
        json={
            'customer_id':1,
            'quantity':1,
            'item_id':2
        }
    )
    print(res.json())
    assert res.status_code == status.HTTP_201_CREATED

def test_make_orders_to_an_item_that_does_not_exist(authorized_client, create_multiple_test_items):
    res = authorized_client.post(
        '/orders/10',
        json={
            'customer_id':1,
            'quantity':1,
            'item_id':10
        }
    )
    assert res.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR


def test_oders_made_endpoint(authorized_client, create_multiple_orders):
    res = authorized_client.get(
        '/orders'
    )
    print(res.json())
    assert res.status_code == status.HTTP_200_OK

def test_get_orders_made_without_auth(client, create_multiple_orders):
    res = client.get(
        '/orders'
    )
    assert res.status_code == status.HTTP_401_UNAUTHORIZED