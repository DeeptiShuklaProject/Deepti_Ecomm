from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Define the database URL
DATABASE_URL = "postgresql+psycopg2://postgres:deepti@localhost:5432/Deepti_ecom"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Define the Base class
Base = declarative_base()

# Define your models
class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    orders = relationship('Order', back_populates='customer')

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    order_items = relationship('OrderItem', back_populates='product')

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    customer = relationship('Customer', back_populates='orders')
    items = relationship('OrderItem', back_populates='order')

class OrderItem(Base):
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    order = relationship('Order', back_populates='items')
    product = relationship('Product', back_populates='order_items')

# Drop existing tables (optional)
Base.metadata.drop_all(engine)

# Create all tables
Base.metadata.create_all(engine)

# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

# Optionally: Add sample data
def add_sample_data():
    # Example data
    customers = [
        Customer(name='John Doe', email='john@example.com'),
        Customer(name='Jane Smith', email='jane@example.com')
    ]

    products = [
        Product(name='Laptop', price=1000),
        Product(name='Smartphone', price=500)
    ]

    session.add_all(customers)
    session.add_all(products)
    session.commit()

    orders = [
        Order(customer=customers[0], items=[OrderItem(product=products[0], quantity=1)]),
        Order(customer=customers[1], items=[OrderItem(product=products[1], quantity=2)])
    ]

    session.add_all(orders)
    session.commit()

add_sample_data()

print("Database initialized and sample data added.")
