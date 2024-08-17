# app/crud.py

from sqlalchemy.orm import Session
from .models import Customer, Product, Order, OrderItem

def create_customer(db: Session, name: str, email: str):
    customer = Customer(name=name, email=email)
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer

def create_product(db: Session, name: str, price: float, quantity: int):
    product = Product(name=name, price=price, quantity=quantity)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def create_order(db: Session, customer_id: int, order_data: list):
    order = Order(customer_id=customer_id)
    db.add(order)
    db.commit()
    db.refresh(order)
    
    for item in order_data:
        order_item = OrderItem(order_id=order.id, product_id=item["product_id"], quantity=item["quantity"])
        db.add(order_item)
    
    db.commit()
    return order

def get_customer(db: Session, customer_id: int):
    return db.query(Customer).filter_by(id=customer_id).first()

def get_product(db: Session, product_id: int):
    return db.query(Product).filter_by(id=product_id).first()

def get_order(db: Session, order_id: int):
    return db.query(Order).filter_by(id=order_id).first()
