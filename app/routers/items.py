from sqlalchemy.orm import session
from fastapi import APIRouter
from fastapi import status, Depends, HTTPException
from app.schema import schema
from app.database.database import get_db
from app.models import models
from typing import List


router: APIRouter =  APIRouter(
    prefix = '/items',
    tags = ['Items in Store']
)

@router.post('', status_code=status.HTTP_201_CREATED, response_model=schema.ItemResponse)
def create_an_item(item:schema.ItemCreate, db:session =Depends(get_db)):
    new_item = models.Items(**item.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@router.get('', status_code=status.HTTP_200_OK,response_model=List[schema.ItemResponse])
def get_all_items(db:session =Depends(get_db)):
    items = db.query(models.Items).all()
    if not items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='no item found')
    return items


    
@router.get('/{item_id}', status_code=status.HTTP_200_OK, response_model=schema.ItemResponse)
def get_one_item(item_id:int, db:session=Depends(get_db)):
    item = db.query(models.Items).filter(models.Items.item_id == item_id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='no item found')
    return item 

@router.put('/{item_id}', status_code=status.HTTP_200_OK ,response_model=schema.ItemResponse)
def update_an_item(item_id:int, item_update:schema.ItemCreate, db:session=Depends(get_db)):
    item_query = db.query(models.Items).filter(models.Items.item_id == item_id)
    item = item_query.first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=' item not found')
    item_query.update(item_update.dict(), synchronize_session=False)
    db.commit()
    return item_query.first()

    
@router.delete('/{item_id}', status_code=status.HTTP_200_OK, response_model=schema.ItemDeleteResponse)
def delete_an_item(item_id:int, db:session=Depends(get_db), ):
    item_query = db.query(models.Items).filter(models.Items.item_id == item_id)
    if not item_query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='item does not exist')
    item_query.delete(synchronize_session=False)
    db.commit()
    return schema.ItemDeleteResponse(message='item deleted successfully')

