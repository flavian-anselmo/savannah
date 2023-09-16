from fastapi import status
from app.schema import schema
import pytest


def test_create_item_endpoint(authorized_client):
    res = authorized_client.post(
        '/items',
        json={
            'item_id':1,
            'item_name':'test_item',
            'item_stock':9,
            'price':50.0
        }
    )
    new_item = schema.ItemResponse(
        **res.json()
    )
    print(res.json())
    assert new_item.item_stock == 9
    assert res.status_code ==status.HTTP_201_CREATED

def test_get_all_items(authorized_client, create_multiple_test_items):
    res = authorized_client.get(
        '/items'
    )
    print(res.json())
    assert res.status_code == status.HTTP_200_OK
    assert len(res.json()) == len(create_multiple_test_items)

def test_get_all_items_not_found(authorized_client):
    res = authorized_client.get(
        '/items'
    )
    print(res.json())
    res.json()['detail'] == 'no item found'
    assert res.status_code == status.HTTP_404_NOT_FOUND

def test_get_one_item(authorized_client, create_a_test_item):
    res =authorized_client.get(
        '/items/1'
    )
    assert res.status_code == status.HTTP_200_OK

def test_get_one_item_not_found(authorized_client):
    res =authorized_client.get(
        '/items/2'
    )
    assert res.json()['detail'] == 'no item found'
    assert res.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.skip()
def test_update_item(authorized_client, create_a_test_item):
    res = authorized_client.put(
        '/item/1',
        json={
            'item_id':1,
            'item_name':'test_item_update',
            'item_stock':9,
            'price':50.0
        }
    )
    update = schema.ItemResponse(
        **res.json()
    )
    assert update.item_name =='test_item_update'
    assert res.status_code == status.HTTP_201_CREATED



