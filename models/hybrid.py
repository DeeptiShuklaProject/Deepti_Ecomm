from models.collaborative_filtering import collaborative_filtering
from models.content_based import content_based

def hybrid_model(user_id, n_recommendations=5):
    # Get recommendations from collaborative filtering
    collab_recs = collaborative_filtering(user_id, n_recommendations)
    
    # Get recommendations from content-based filtering
    content_recs = content_based(user_id, n_recommendations)
    
    # Combine the recommendations and remove duplicates
    combined_recs = collab_recs + content_recs
    combined_recs = list(dict.fromkeys(combined_recs))  # Remove duplicates while preserving order
    
    # Truncate the combined list to the desired number of recommendations
    if len(combined_recs) > n_recommendations:
        combined_recs = combined_recs[:n_recommendations]
    
    return combined_recs
