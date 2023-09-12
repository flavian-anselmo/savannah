from fastapi import APIRouter,Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import session
from app.schema import schema
from app.models import models
from app.oauth import oauth2
from app.utils import auth_utils
from app.database.database import get_db


router = APIRouter(
    prefix='/auth',
    tags=['Customer Authentication']
)



@router.post('/sign-in',status_code=status.HTTP_200_OK, response_model = schema.TokenResponse)
def sign_in(customer_creds: OAuth2PasswordRequestForm = Depends(), db:session = Depends(get_db)):
    customer = db.query(models.Customers).filter(models.Customers.customer_name == customer_creds.username).first()

    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User Does not exist')
        
    if not auth_utils.verify_password(customer_creds.password, customer.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Invalid credentials ')

    access_token = oauth2.create_access_token(payload = {"customer_id": customer.customer_id})
    return schema.TokenResponse(access_token = access_token, type = "Bearer") 

    

@router.post('/sign-up', status_code=status.HTTP_201_CREATED, response_model=schema.CustomerResponse)    
def sign_up(customer:schema.CustomerCreate,db:session=Depends(get_db)):
    hash_password  = auth_utils.get_hashed_password(str(customer.password))
    customer.password = hash_password
    customer_phone_check = db.query(models.Customers).filter(models.Customers.phone_no == customer.phone_no).first()
    if customer_phone_check:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Phone Number already exists')
  
    new_customer = models.Customers(**customer.dict())
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer
