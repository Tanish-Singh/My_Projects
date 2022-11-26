#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 11:13:55 2022

@author: tanishsingh
"""

import numpy as np
import pandas as pd
import joblib

df=pd.read_csv('insurance.csv')

print(df.isna().sum())


df=df.dropna()

x=df.iloc[:,:-1]
y=df['charges']



from sklearn.preprocessing import LabelEncoder


le=LabelEncoder()
x['gender']=le.fit_transform(x['gender'])

lo=LabelEncoder()
x['smoker']=lo.fit_transform(x['smoker'])





from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct=ColumnTransformer([('encoder',OneHotEncoder(),[5])],remainder='passthrough')
x=ct.fit_transform(x)


from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x=sc.fit_transform(x)
joblib.dump(sc,'scaler.joblib')



from sklearn.model_selection import train_test_split as tts
x_train,x_test,y_train,y_test=tts(x,y,test_size=0.2)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)
y_pred=regressor.predict(x_test)
from sklearn.metrics import r2_score
print(r2_score(y_test,y_pred))



joblib.dump(regressor,'regressor.joblib')











