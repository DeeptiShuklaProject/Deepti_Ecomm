import pandas as pd

def load_raw_data():
    user_data = pd.read_csv('data/raw/user_data.csv')
    product_data = pd.read_csv('data/raw/product_data.csv')
    transactions = pd.read_csv('data/raw/transactions.csv')
    return user_data, product_data, transactions

def preprocess_data(user_data, product_data, transactions):
    # Example processing step: merging data to create user-product interactions
    user_product_interactions = transactions.merge(user_data, on='user_id').merge(product_data, on='product_id')
    
    # Extracting user and product features
    user_features = user_data[['user_id', 'age', 'gender', 'location']]
    product_features = product_data[['product_id', 'product_name', 'category', 'price']]
    
    # Saving processed data
    user_product_interactions.to_csv('data/processed/user_product_interactions.csv', index=False)
    user_features.to_csv('data/processed/user_features.csv', index=False)
    product_features.to_csv('data/processed/product_features.csv', index=False)

def main():
    user_data, product_data, transactions = load_raw_data()
    preprocess_data(user_data, product_data, transactions)

if __name__ == "__main__":
    main()
