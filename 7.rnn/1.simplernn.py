import tensorflow as tf
from tensorflow.keras.layers import *
from tensorflow.keras.models import *
from tensorflow.keras.datasets import imdb

(train_x, train_y), (test_x, test_y) = imdb.load_data(num_words=1000)
print("Review is : ", train_x[5])
print("Label is : ", train_y[5])

vocab = imdb.get_word_index()
print(vocab)

from keras_preprocessing import sequence
max_words = 500
train_x = sequence.pad_sequences(train_x, maxlen = max_words)
test_x = sequence.pad_sequences(test_x, maxlen = max_words)

embedding_size = 32
model = Sequential()
model.add(Embedding(1000, embedding_size, input_length=(max_words)))
model.add(SimpleRNN(100, return_sequences='true'))
model.add(SimpleRNN(50, return_sequences='true'))
model.add(SimpleRNN(25))
model.add(Dense(1, activation='sigmoid'))
print(model.summary())

model.compile(optimizer = 'rmsprop', loss = 'binary_crossentropy', metrics  =['acc'])
history = model.fit(train_x, train_y, epochs=10, batch_size=120, validation_split=0.2)

import matplotlib.pyplot as plt
def plot_graphs(history, string):
    plt.plot(history.history[string])
    plt.plot(history.history['val_'+string])
    plt.xlabel("Epochs")
    plt.ylabel(string)
    plt.legend([string, 'val_'+string])
    plt.show()
plot_graphs(history, 'acc')
plot_graphs(history, 'loss')
