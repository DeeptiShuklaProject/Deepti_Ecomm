from utils.metrics import precision_at_k, recall_at_k, f1_score_at_k

def evaluate_model(user_id, recommendations, interactions):
    # Get actual items interacted by the user
    user_interactions = interactions[interactions['user_id'] == user_id]
    relevant_items = user_interactions['product_id'].unique().tolist()
    
    k = len(recommendations)
    precision = precision_at_k(recommendations, relevant_items, k)
    recall = recall_at_k(recommendations, relevant_items, k)
    f1 = f1_score_at_k(precision, recall)
    
    return {
        'precision': precision,
        'recall': recall,
        'f1_score': f1
    }
