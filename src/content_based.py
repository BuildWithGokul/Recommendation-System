from sklearn.metrics.pairwise import cosine_similarity

def content_recommend(mat, data, item, top_n=3):
    idx = data[data['item_name'] == item].index[0]
    sim = cosine_similarity(mat)
    scores = sorted(list(enumerate(sim[idx])), key=lambda x: x[1], reverse=True)
    return [data.iloc[i[0]]['item_name'] for i in scores[1:top_n+1]]

