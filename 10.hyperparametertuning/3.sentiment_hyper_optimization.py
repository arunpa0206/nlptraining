import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM,Dense, Dropout, SpatialDropout1D, Activation
from tensorflow.keras.layers import Embedding
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras.optimizers import SGD, Adam, RMSprop

from hyperopt import Trials, STATUS_OK, tpe
from hyperas import optim
from hyperas.distributions import choice, uniform
import numpy as np
from hyperas import optim
from hyperas.distributions import choice, uniform

import _locale 
_locale._getdefaultlocale = (lambda *args: ['en_US', 'utf8'])

def data():
    #load the csv file into the dataframe
    df = pd.read_csv("Tweets.csv")
    #pick the text and airline sentiment
    tweet_df = df[['text','airline_sentiment']]
    #Pick rows with sentiment not nuetral
    tweet_df = tweet_df[tweet_df['airline_sentiment'] != 'neutral']
    #print(tweet_df)

    #factorize method generates a numerical value for each catagory
    sentiment_label = tweet_df.airline_sentiment.factorize()
    #tokenize the tweets
    tweet = tweet_df.text.values
    tokenizer = Tokenizer(num_words=5000)
    tokenizer.fit_on_texts(tweet)
    #print(tokenizer.word_index)

    #vocabolary size is the number of tokens
    vocab_size = len(tokenizer.word_index) + 1
    #transform each text to sequence of integers
    encoded_docs = tokenizer.texts_to_sequences(tweet)
    #Every tweet is padded to have a total length of 200
    padded_sequence = pad_sequences(encoded_docs, maxlen=200)
    #rint(padded_sequence)
    X_train, X_val, y_train, y_val = train_test_split(padded_sequence, sentiment_label[0], test_size=0.2, random_state=12345)
    
    #print(len(X_train))
    #print(len(X_val))
    # print(len(y_train))
    # print(len(y_val))
    
    return X_train, X_val, y_train, y_val
    
def create_model(X_train, y_train, X_val, y_val):
    #create embedded vecttor length of 32 
    embedding_vector_length = 32
    model = Sequential()
    #Use the input length of padded length 200 to form vectors for each word in the vocalobary 
    model.add(Embedding(len(X_train), embedding_vector_length, input_length=200) )
    #drop out reduces overfitting.
    model.add(SpatialDropout1D({{uniform(0, 0.5)}})) 
    #add lstm layer with drop out.
    model.add(LSTM({{choice([50,100,200])}},dropout={{uniform(0, 1)}} ,recurrent_dropout={{uniform(0, 1)}})) 
    model.add(Dropout({{uniform(0, 1)}}))
    #add a fully connected layer
    model.add(Dense(1, activation='sigmoid')) 
    
    # Setting Optimizer choices:
    adam = keras.optimizers.Adam(lr={{choice([10**-3, 10**-2, 10**-1])}})
    rmsprop = keras.optimizers.RMSprop(lr={{choice([10**-3, 10**-2, 10**-1])}})
    sgd = keras.optimizers.SGD(lr={{choice([10**-3, 10**-2, 10**-1])}})
    choiceval = {{choice(['adam', 'sgd', 'rmsprop'])}}
    if choiceval == 'adam':
        optim = adam
    elif choiceval == 'rmsprop':
        optim = rmsprop
    else:
        optim = sgd


    model.compile(loss='binary_crossentropy',optimizer=optim, metrics=['accuracy'])  
    print(model.summary())
    
    #get accuracy for 5 epochs with batch size of32
    history = model.fit(X_train, y_train,validation_split=0.2, epochs=5, batch_size={{choice([16,32,64])}}, verbose=1)
    
    score, acc = model.evaluate(X_val, y_val, verbose=0)
    print('Test accuracy:', acc)
    return {'loss': -acc, 'status': STATUS_OK, 'model': model}
    
X_train, y_train, X_val, y_val = data() 
best_run, best_model = optim.minimize(model=create_model,
                                          data=data,
                                          algo=tpe.suggest,
                                          max_evals=5,
                                          trials=Trials()
                                          )
