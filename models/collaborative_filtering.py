import pandas as pd
from sklearn.decomposition import TruncatedSVD
import numpy as np

def collaborative_filtering(user_id, n_recommendations=5):
    interactions = pd.read_csv('data/processed/user_product_interactions.csv')
    
    # Create user-product interaction matrix
    user_product_matrix = interactions.pivot_table(
        index='user_id', 
        columns='product_id', 
        values='interaction_value', 
        fill_value=0
    )
    
    # Fit SVD model
    n_components = min(3, user_product_matrix.shape[1] - 1) or 1
    svd = TruncatedSVD(n_components=n_components)
    latent_matrix = svd.fit_transform(user_product_matrix)
    
    # Create a DataFrame for latent features
    latent_df = pd.DataFrame(latent_matrix, index=user_product_matrix.index)
    
    # Compute cosine similarity
    user_similarity = np.dot(latent_df, latent_df.T)
    user_similarity_df = pd.DataFrame(user_similarity, index=user_product_matrix.index, columns=user_product_matrix.index)
    
    # Get similar users
    similar_users = user_similarity_df[user_id].sort_values(ascending=False)[1:]
    
    # Get products that similar users have interacted with
    similar_users_interactions = user_product_matrix.loc[similar_users.index]
    recommended_products = similar_users_interactions.mean().sort_values(ascending=False)
    
    # Filter out products the user has already interacted with
    user_interacted_products = user_product_matrix.loc[user_id]
    recommended_products = recommended_products[user_interacted_products == 0]
    
    # Get top-N recommendations
    top_recommendations = recommended_products.head(n_recommendations).index.tolist()
    
    return top_recommendations
