# app/schemas.py

from pydantic import BaseModel
from typing import List

class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int

class OrderCreate(BaseModel):
    customer_id: int
    items: List[OrderItemCreate]

class CustomerCreate(BaseModel):
    name: str
    email: str

class ProductCreate(BaseModel):
    name: str
    price: float
    quantity: int

class Customer(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True

class Product(BaseModel):
    id: int
    name: str
    price: float
    quantity: int

    class Config:
        orm_mode = True

class OrderItem(BaseModel):
    id: int
    product_id: int
    quantity: int

    class Config:
        orm_mode = True

class Order(BaseModel):
    id: int
    customer_id: int
    items: List[OrderItem]

    class Config:
        orm_mode = True
