def precision_at_k(recommended_items, relevant_items, k):
    recommended_at_k = recommended_items[:k]
    relevant_set = set(relevant_items)
    recommended_set = set(recommended_at_k)
    intersection = recommended_set.intersection(relevant_set)
    precision = len(intersection) / k
    return precision

def recall_at_k(recommended_items, relevant_items, k):
    recommended_at_k = recommended_items[:k]
    relevant_set = set(relevant_items)
    recommended_set = set(recommended_at_k)
    intersection = recommended_set.intersection(relevant_set)
    recall = len(intersection) / len(relevant_items) if relevant_items else 0
    return recall

def f1_score_at_k(precision, recall):
    if precision + recall == 0:
        return 0
    return 2 * (precision * recall) / (precision + recall)
