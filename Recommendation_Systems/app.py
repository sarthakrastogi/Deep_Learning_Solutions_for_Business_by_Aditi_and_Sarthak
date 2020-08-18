import numpy as np
import pandas as pd
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def create_sim():
    data = pd.read_csv('products_data_aditi.csv')
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(data['comb'])
    sim = cosine_similarity(count_matrix)
    return data,sim

def rec2(m):
    prod = prod.lower()
    try:
        data.head()
        sim.shape
    except:
        data, sim = create_sim()
    if m not in data['Product_name'].unique():
        return('No such product.')
    else:
        i = data.loc[data['Product_name']==prod].index[0]

        lst = list(enumerate(sim[i]))
        lst = sorted(lst, key = lambda x:x[1] ,reverse=True)
        lst = lst[1:11]
        l = []
        for i in range(len(lst)):
            a = lst[i][0]
            l.append(data['Product_name'][a])
        return l

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/recommender")
def recommend():
    prod = request.args.get('prod')
    r = rec2(prod)
    if type(r)==type('string'):
        return render_template('recommender.html',prod=prod,r=r,t='s')
    else:
        return render_template('recommender.html',prod=prod,r=r,t='l')

if __name__ == '__main__':
    app.run()
