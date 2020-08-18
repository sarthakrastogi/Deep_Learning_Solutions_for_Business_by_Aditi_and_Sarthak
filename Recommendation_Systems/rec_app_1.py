import pandas as pd
import numpy as np

from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

vectorizer = TfidfVectorizer(stop_words='english')
X1 = vectorizer.fit_transform(df2["product_description"])
X1
X=X1

kmeans = KMeans(n_clusters = 10, init = 'k-means++')
y_kmeans = kmeans.fit_predict(X)

def print_cluster(i):
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :6]:
        print(' %s' % terms[ind]),
    print

true_k = 10
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X1)
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()

import pickle
filename = 'rec_model1.sav'
loaded_model = pickle.load(open(filename, 'rb'))
def recommend(product):
    Y = vectorizer.transform([product])
    prediction = loaded_model.predict(Y)
    print_cluster(prediction[0])
recommend(product_input)