import numpy as np
import pandas as pd
df = pd.read_csv('creditcard.csv')
X = df.drop(['Class'], axis = 1)
y = df['Class']
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X, y, test_size=0.1)
from sklearn.ensemble import RandomForestClassifier
model6 = RandomForestClassifier()
model6.fit(X_train,y_train)
pred=model6.predict(transaction_det)
if pred == 0:
	print('Stopping transaction.')
	break
elif pred == 1:
	continue


