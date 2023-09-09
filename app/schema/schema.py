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
