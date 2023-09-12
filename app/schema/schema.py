from pydantic import BaseModel, validator
import re as regex 
from datetime import datetime

class ItemCreate(BaseModel):
    item_name:str
    item_stock:int
    price: float
class ItemResponse(BaseModel):
    item_id: int
    item_name:str
    item_stock:int
    price: float
    class Config:
        orm_mode = True


class ItemDeleteResponse(BaseModel):
    message:str 
    class Config:
        orm_mode = True

class TokenPayLoad(BaseModel):
    customer_id:int
class TokenResponse(BaseModel):
    access_token:str
    type:str


class CustomerCreate(BaseModel):
    customer_name: str
    phone_no:str
    password:str

    # validation 
    @validator('password')
    def validate_paswd(cls, password:str):
        if len(password) < 8:
            raise ValueError('password is weak, it should be 8 characters and above')
        
    @validator('phone_no')
    def validate_phone_no(cls, phone_no:str):
        pattern = r'^\+254\d{9}$'
        if regex.match(pattern, phone_no):
            return phone_no
        raise ValueError('phone number should start with +254 format')
        
class CustomerResponse(BaseModel):
    customer_id:int 
    customer_name: str
    phone_no:str
    class Config:
        orm_mode = True

class OrdersCreate(BaseModel):
    quantity:int


class OrdersResponse(BaseModel):
    order_id:int 
    created_at: datetime
    customer: CustomerResponse
    item: ItemResponse
    class Config:
        orm_mode = True

class OrderResponseBeforeMsgSent(BaseModel):
    message:str

