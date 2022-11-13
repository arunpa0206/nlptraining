import tensorflow as tf
from tensorflow.keras.layers import *
from tensorflow.keras.models import *
from tensorflow.keras.datasets import imdb
import pandas as pd
import matplotlib.pyplot as plt
import keras
from keras import *

from hyperopt import Trials, STATUS_OK, tpe
from hyperas import optim
from hyperas.distributions import choice, uniform
import numpy as np
from hyperas import optim
from hyperas.distributions import choice, uniform

import _locale 
_locale._getdefaultlocale = (lambda *args: ['en_US', 'utf8'])

def data():
    (x_train, y_train), (x_val, y_val) = imdb.load_data(num_words=1000)
    #print("Review is : ", train_x[5])
    #print("Label is : ", train_y[5])
    
    vocab = imdb.get_word_index()
    #print(vocab)
    
    from keras_preprocessing import sequence
    max_words = 500
    # In order to feed data in RNN, all input-docs must have the same length. We limit the max
    # review length to max_words by truncating longer reviews and padding shorter reviews with '0's at the end.
    x_train = sequence.pad_sequences(x_train, maxlen = max_words)
    x_val = sequence.pad_sequences(x_val, maxlen = max_words)

    
    return x_train, x_val, y_train, y_val
    
def create_model(x_train, y_train, x_val, y_val):
    embedding_size = 32
    model = Sequential()
    model.add(Embedding(1000, embedding_size, input_length=(max_words)))
    model.add(SimpleRNN({{choice([50,100])}}, {{choice(['true', 'false'])}})) # return_sequences='true'
    model.add(SimpleRNN({{choice([25,50])}}, {{choice(['true', 'false'])}})) # return_sequences='true'
    # when the return_sequences is set to true, the prev timesteps of the rnn input produces an output
    # that can be consumed by full-connected layer.
    model.add(SimpleRNN({{choice([25,50])}}))
    model.add(Dense(1, activation='sigmoid'))
    print(model.summary())
    
    
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
    history = model.fit(x_train, y_train,validation_split={{choice([0.2,0.3])}}, epochs={{choice([5,10])}}, batch_size={{choice([60,120])}}, verbose=1)
    
    score, acc = model.evaluate(x_val, y_val, verbose=1)
    print('Test accuracy:', acc)
    return {'loss': -acc, 'status': STATUS_OK, 'model': model}
    
    
    
x_train, y_train, x_val, y_val = data() 
best_run, best_model = optim.minimize(model=create_model,
                                          data=data,
                                          algo=tpe.suggest,
                                          max_evals=2,
                                          trials=Trials()
                                          )
