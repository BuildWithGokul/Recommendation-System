from src.data_loader import load_data
from src.preprocessing import create_item_profiles
from src.recommender import recommend_system
data = load_data('data/dataset.csv')
matrix,_ = create_item_profiles(data)
print('Content Based:', recommend_system(data,matrix,'content','Python Course'))
print('Collaborative:', recommend_system(data,matrix,'collaborative',1))
