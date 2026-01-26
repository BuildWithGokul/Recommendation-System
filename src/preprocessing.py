from sklearn.feature_extraction.text import TfidfVectorizer

def create_item_profiles(data):
    data['text'] = data['item_name'] + ' ' + data['category']
    tfidf = TfidfVectorizer()
    mat = tfidf.fit_transform(data['text'])
    return mat, tfidf


