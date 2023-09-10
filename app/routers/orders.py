from fastapi import APIRouter
from app.schema import schema
from fastapi import status, Depends, HTTPException
from sqlalchemy.orm import session
from app.database.database import get_db
from app.oauth.oauth2 import get_current_user_logged_in
from app.models import models




router: APIRouter =  APIRouter(
    prefix = '/orders',
    tags = ['Customer Orders']
)

@router.post('', status_code=status.HTTP_200_OK, response_model=schema.OrdersResponse)
def make_an_order( order:schema.OrdersCreate,  db:session=Depends(get_db), current_user = Depends(get_current_user_logged_in)):
    new_order = models.Orders(
        customer_id = current_user.customer_id,
        **order.dict()
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order