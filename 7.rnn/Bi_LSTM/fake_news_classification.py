#Dataset Link - https://drive.google.com/file/d/1s_U9NhGoKQHet7sbw2g7-yu568Ycktaq/view?usp=sharing
import pandas as pd
df=pd.read_csv('train.csv')
print(df.head())

###Drop Nan Values
df=df.dropna()
## Get the Independent Features

X=df.drop('label',axis=1)
## Get the Dependent features
y=df['label']
#y.value_counts()

print(X.shape)
print(y.shape)

import tensorflow as tf
from tensorflow.keras.layers import Embedding
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Bidirectional
from tensorflow.keras.layers import Dropout
### Vocabulary size
voc_size=5000

messages=X.copy()
#messages['title'][1]

messages.reset_index(inplace=True)
import nltk
import re
from nltk.corpus import stopwords
nltk.download('stopwords')

### Dataset Preprocessing
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
corpus = []
for i in range(0, len(messages)):
    #print(i)
    review = re.sub('[^a-zA-Z]', ' ', messages['title'][i])
    review = review.lower()
    review = review.split()
    
    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    corpus.append(review)

#print(corpus)

onehot_repr=[one_hot(words,voc_size)for words in corpus] 
#print(onehot_repr)

sent_length=20
embedded_docs=pad_sequences(onehot_repr,padding='pre',maxlen=sent_length)
#print(embedded_docs)

#print(embedded_docs[0])

## Creating model
embedding_vector_features=40
model1=Sequential()
model1.add(Embedding(voc_size,embedding_vector_features,input_length=sent_length))
model1.add(Bidirectional(LSTM(100)))
model1.add(Dropout(0.3))
model1.add(Dense(1,activation='sigmoid'))
model1.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
print(model1.summary())


import numpy as np
X_final=np.array(embedded_docs)
y_final=np.array(y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_final, y_final, test_size=0.33, random_state=42)

### Finally Training
model1.fit(X_train,y_train,validation_data=(X_test,y_test),epochs=10,batch_size=64)

predict_x = model1.predict(X_test) 
y_pred1 = np.argmax(predict_x,axis=1)

from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_pred1))

from sklearn.metrics import accuracy_score
print("Accuracy Score -> " + str(accuracy_score(y_test,y_pred1)))


from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred1))
