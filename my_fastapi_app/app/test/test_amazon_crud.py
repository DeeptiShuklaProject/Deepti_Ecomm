# app/test/test_amazon_crud.py

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app, get_db
from app.database import Base
from app.models import Customer, Product, Order

# Setup the database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Using SQLite for testing

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

# Dependency override for tests
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(scope="module")
def test_db():
    # Create a new database for the test
    Base.metadata.create_all(bind=engine)
    yield TestingSessionLocal()
    Base.metadata.drop_all(bind=engine)

def test_placeholder():
    assert True

def test_create_customer(test_db):
    response = client.post("/customers/", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john.doe@example.com"

def test_create_product(test_db):
    response = client.post("/products/", json={"name": "Laptop", "price": 1200.00, "quantity": 10})
    assert response.status_code == 200
    assert response.json()["name"] == "Laptop"
    assert response.json()["price"] == 1200.00
    assert response.json()["quantity"] == 10

def test_create_order(test_db):
    # Create a customer first
    response = client.post("/customers/", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    customer_id = response.json()["id"]

    # Create a product
    response = client.post("/products/", json={"name": "Smartphone", "price": 800.00, "quantity": 5})
    product_id = response.json()["id"]

    # Create an order
    order_data = {"customer_id": customer_id, "items": [{"product_id": product_id, "quantity": 2}]}
    response = client.post("/orders/", json=order_data)
    assert response.status_code == 200
    assert response.json()["customer_id"] == customer_id
    assert len(response.json()["items"]) == 1
    assert response.json()["items"][0]["product_id"] == product_id

def test_read_customer(test_db):
    response = client.get("/customers/1")
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"

def test_read_product(test_db):
    response = client.get("/products/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Laptop"

def test_read_order(test_db):
    response = client.get("/orders/1")
    assert response.status_code == 200
    assert response.json()["customer_id"] == 1
