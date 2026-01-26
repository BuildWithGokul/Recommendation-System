from sklearn.metrics.pairwise import cosine_similarity

def collaborative_recommend(data, user_id, top_n=3):
    user_item = data.pivot_table(index='user_id', columns='item_name', values='rating').fillna(0)
    sim = cosine_similarity(user_item)
    idx = list(user_item.index).index(user_id)
    scores = sorted(list(enumerate(sim[idx])), key=lambda x: x[1], reverse=True)
    users = [user_item.index[i[0]] for i in scores[1:]]
    recs = data[data['user_id'].isin(users)].groupby('item_name')['rating'].mean().sort_values(ascending=False)
    return list(recs.head(top_n).index)

