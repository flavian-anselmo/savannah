from fastapi import APIRouter
from app.schema import schema
from fastapi import status, Depends, HTTPException
from sqlalchemy.orm import session
from app.database.database import get_db
from app.oauth.oauth2 import get_current_user_logged_in
from app.models import models
from app.tasks.sms_bg_task import SmsTaks
from fastapi import BackgroundTasks
from typing import List




router: APIRouter =  APIRouter(
    prefix = '/orders',
    tags = ['Customer Orders']
)

@router.post('/{item_id}', status_code=status.HTTP_201_CREATED, response_model=schema.OrderResponseBeforeMsgSent)
async def make_an_order(item_id:int, background_task:BackgroundTasks, order:schema.OrdersCreate,  db:session=Depends(get_db), current_user = Depends(get_current_user_logged_in)):
    try:
        new_order = models.Orders(
            customer_id = current_user.customer_id,
            item_id= item_id,
            **order.dict()
        )
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'Db error: {str(err)}')
    
    if not new_order:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='order was not created')

    background_task.add_task(
        # BACKGROUND TASK FOR SMS 
        SmsTaks.send_sms_for_orders,
        phone_no = current_user.phone_no,
        customer_name = current_user.customer_name
    )
    return schema.OrderResponseBeforeMsgSent(
        message= f'Confirmation message for your Order will be sent shortly via {current_user.phone_no}'
    )

@router.get('', status_code=status.HTTP_200_OK, response_model=List[schema.OrdersResponse])
def get_orders_made(db:session=Depends(get_db), current_user = Depends(get_current_user_logged_in)):
    order = db.query(models.Orders).filter(models.Orders.customer_id == current_user.customer_id).all()
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Hey {current_user.customer_name}, You have not made any orders ')
    return order
