from pydantic import BaseModel


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
    customer_id:int 
    customer_name: str
    phone_no:str
    password:str


class CustomerResponse(BaseModel):
    customer_id:int 
    customer_name: str
    phone_no:str
    password:str
    class Config:
        orm_mode = True

