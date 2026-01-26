from src.content_based import content_recommend
from src.collaborative import collaborative_recommend

def recommend_system(data, item_matrix, mode, value):
    if mode == 'content':
        return content_recommend(item_matrix, data, value)
    elif mode == 'collaborative':
        return collaborative_recommend(data, value)
    else:
        return []

