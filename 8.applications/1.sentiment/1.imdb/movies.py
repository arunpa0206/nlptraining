import numpy as  numpy
from keras.datasets import imdb
from matplotlib import pyplot

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from tensorflow.keras.layers import Embedding
from keras.utils import pad_sequences
import warnings
warnings.filterwarnings('ignore')

# call load_data with allow_pickle implicitly set to true
#(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000
# load the dataset
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=5000)
X = numpy.concatenate((X_train, X_test), axis=0)
y = numpy.concatenate((y_train, y_test), axis=0)

print("X[0]:",X[0])
print("Y[0]:",y[0])

# summarize size
#print("Training data: ")
print("X.shape:",X.shape)
print("Y.shape:",y.shape)

print("Classes: ")
#print(numpy.unique(y))
print("Number of words: ")
print("length:",len(numpy.unique(numpy.hstack(X))))

# Summarize review length
print("Review length: ")
result = [len(x) for x in X]
print("Mean %.2f review length (%f)" % (numpy.mean(result), numpy.std(result)))

top_words = 5000
max_words = 500
X_train = pad_sequences(X_train, maxlen=max_words)
X_test = pad_sequences(X_test, maxlen=max_words)

model = Sequential()
model.add(Embedding(top_words, 32, input_length=max_words))
model.add(Flatten())
model.add(Dense(250, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=2, batch_size=128, verbose=2)
# Final evaluation of the model
scores = model.evaluate(X_test, y_test, verbose=0)
print("Accuracy: %.2f%%" % (scores[1]*100))
