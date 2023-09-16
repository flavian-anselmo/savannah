from fastapi import status
from app.schema import schema
import pytest



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


def test_oders_made_endpoint(authorized_client, create_multiple_orders):
    res = authorized_client.get(
        '/orders'
    )
    print(res.json())
    assert res.status_code == status.HTTP_200_OK

