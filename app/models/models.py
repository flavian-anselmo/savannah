from sqlalchemy.orm import relationship
from app.database.database import Base
from sqlalchemy.sql.expression import text
from sqlalchemy import Column,ForeignKey,Integer,String,Float,TIMESTAMP


class Customers(Base):
    '''
    customer records 
    '''
    __tablename__ = 'customers'
    customer_id = Column(Integer, primary_key=True, nullable=False)
    customer_name = Column(String, nullable=False)
    phone_no = Column(String, nullable=False)
    password = Column(String, nullable = False)


class Orders(Base):
    '''
    Orders made by customers to buy items from items table

    '''
    __tablename__ = 'orders'
    order_id = Column(Integer, primary_key=True, nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.customer_id', ondelete ="CASCADE"), nullable=False)
    customer = relationship('Customers')
    item_id = Column(Integer, ForeignKey('items.item_id', ondelete ="CASCADE"), nullable=False)
    item = relationship('Items')
    quantity = Column(Integer, nullable = False)
    created_at =  Column (TIMESTAMP(timezone = True), nullable = False, server_default = text('now()'))


class Items(Base):
    '''
    items for customers to buy 

    '''
    __tablename__ = 'items'
    item_id = Column(Integer, primary_key=True, nullable=False)
    item_name = Column(String, nullable=False)
    item_stock = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)

