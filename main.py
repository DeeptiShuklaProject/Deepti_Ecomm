from models import init_db, SessionLocal
from crud import create_customer, create_product, create_order
from sqlalchemy.exc import IntegrityError
from sqlalchemy import text

def clear_db(session):
    """Clear existing data from the database."""
    try:
        session.execute(text("TRUNCATE TABLE order_items, orders, products, customers CASCADE"))
        session.commit()
    except Exception as e:
        print(f"An error occurred while clearing the database: {e}")
        session.rollback()

def main():
    init_db()
    session = SessionLocal()

    # Optional: Clear existing data if needed
    clear_db(session)

    try:
        # Sample Manual Insertion
        customer = create_customer(session, "John Doe", "john@example.com")
        if customer:
            product1 = create_product(session, "Product A", 19.99, 100)
            product2 = create_product(session, "Product B", 29.99, 150)

            order_data = [
                {"product_id": product1.id, "quantity": 2},
                {"product_id": product2.id, "quantity": 1},
            ]
            
            order = create_order(session, customer.id, order_data)
            print(f"Order created: {order.id}")
    except IntegrityError as e:
        print(f"An error occurred: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    main()
