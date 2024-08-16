import pytest
from sqlalchemy.sql import text
from models import init_db, SessionLocal
from crud import create_customer, create_product, create_order, get_customer, get_product, get_order

@pytest.fixture(scope='function')
def db_session():
    # Initialize the database
    init_db()
    session = SessionLocal()
    
    # Clear existing data to avoid conflicts
    try:
        session.execute(text("TRUNCATE TABLE order_items, orders, products, customers CASCADE"))
        session.commit()
    except Exception as e:
        session.rollback()
        raise e

    # Automated data insertion for customers, products, and orders
    customer = create_customer(session, "John Doe", "john@example.com")
    product1 = create_product(session, "Product A", 19.99, 100)
    product2 = create_product(session, "Product B", 29.99, 150)
    product3 = create_product(session, "Product C", 39.99, 200)
    
    order_data = [
        {"product_id": product1.id, "quantity": 2},
        {"product_id": product2.id, "quantity": 1},
    ]
    
    create_order(session, customer.id, order_data)
    
    # Commit the transaction to ensure data is saved
    session.commit()

    # Verify if data is correctly inserted
    assert get_customer(session, 1) is not None
    assert get_product(session, 1) is not None
    assert get_order(session, 1) is not None
    
    yield session
    session.close()

def test_create_customer(db_session):
    customer = create_customer(db_session, "Jane Doe", "jane@example.com")
    assert customer.id is not None
    assert customer.name == "Jane Doe"
    assert customer.email == "jane@example.com"

def test_get_customer(db_session):
    customer = get_customer(db_session, 1)
    assert customer is not None
    assert customer.name == "John Doe"
    assert customer.email == "john@example.com"

def test_create_order(db_session):
    customer = get_customer(db_session, 1)
    product = get_product(db_session, 1)
    order_data = [{"product_id": product.id, "quantity": 1}]
    order = create_order(db_session, customer.id, order_data)
    assert order.id is not None
    assert len(order.order_items) == 1
    assert order.order_items[0].product.name == "Product A"

def test_get_order(db_session):
    order = get_order(db_session, 1)
    assert order is not None
    assert order.id == 1
    assert order.customer.name == "John Doe"
    assert len(order.order_items) == 2
    assert order.order_items[0].product.name == "Product A"
