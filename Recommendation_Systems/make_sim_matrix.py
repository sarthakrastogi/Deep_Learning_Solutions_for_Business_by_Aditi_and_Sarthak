import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer

data = pd.read_csv('products_data_aditi.csv')

cv = CountVectorizer()
count_matrix = cv.fit_transform(data['comb'])
from sklearn.metrics.pairwise import cosine_similarity
sim = cosine_similarity(count_matrix)
np.save('similarity_matrix', sim)