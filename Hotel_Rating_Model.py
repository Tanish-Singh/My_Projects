# natural language processing
#important libraries
import tensorflow as tf
import pandas as pd
import numpy as np
import re
import nltk


nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


#read data
df=pd.read_csv('/Users/tanishsingh/Restaurant_Reviews.tsv',delimiter='\t')

porter=PorterStemmer()
corpus=[]

for i in range(len(df)):
    review=re.sub('[a-zA-Z]',' ',df.iloc[i,0])
    review=review.lower()
    review=review.split()
    allstop=stopwords.words('english')
    allstop.remove('not')
    newreview=[]

    review=[porter.stem(x) for x in review if x not in allstop]

    review=' '.join(review)
    corpus.append(review)
  
#Training Model
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=1500)
x=cv.fit_transform(corpus).toarray()#independant
y=df.iloc[:,1]#dependent

#spliting
from sklearn.model_selection import train_test_split as tts
x_train,x_test,y_train,y_test=tts(x,y,test_size=0.15)

#strategy
from sklearn.naive_bayes import GaussianNB
classifier=GaussianNB()
classifier.fit(x_train, y_train)

y_pred=classifier.predict(x_test)


from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,y_pred))
