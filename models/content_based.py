import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def content_based(user_id, n_recommendations=5):
    interactions = pd.read_csv('data/processed/user_product_interactions.csv')
    product_features = pd.read_csv('data/processed/product_features.csv')
    
    # Create TF-IDF matrix
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(product_features['category'])
    
    # Compute cosine similarity between products
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    
    # Get products the user has interacted with
    user_data = interactions[interactions['user_id'] == user_id]
    user_products = user_data['product_id'].tolist()
    
    # Get indices of these products
    product_indices = [product_features[product_features['product_id'] == pid].index[0] for pid in user_products]
    
    # Compute similarity scores
    sim_scores = cosine_sim[product_indices].mean(axis=0)
    
    # Get top-N recommendations
    sim_scores = list(enumerate(sim_scores))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Filter out products the user has already interacted with
    recommended_indices = [i[0] for i in sim_scores if product_features.iloc[i[0]]['product_id'] not in user_products]
    
    top_recommendations = [product_features.iloc[i]['product_id'] for i in recommended_indices[:n_recommendations]]
    
    return top_recommendations
