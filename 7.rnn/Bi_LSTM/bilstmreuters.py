import numpy as np
from sklearn.metrics import accuracy_score
from keras.datasets import reuters
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, LSTM, Activation, Bidirectional, Embedding
from tensorflow.keras import optimizers
from keras.wrappers.scikit_learn import KerasClassifier

# Words are ranked by how often they occur (in the training set) and only the num_words most frequent words are kept.
num_words = 30000 

# Maximum sequence length. Any longer sequence will be truncated.
maxlen = 50 

test_split = 0.3 
(X_train, y_train), (X_test, y_test) = reuters.load_data(num_words = num_words, maxlen = maxlen, test_split = test_split)

# sequences will be padded to the length of the longest individual sequence
X_train = pad_sequences(X_train, padding = 'post') 
X_test = pad_sequences(X_test, padding = 'post') 

# X_train.shape[0] == 1395 (No of Training Samples)
# X_train.shape[1] == 49 (Size of Training Sample)
# Reshaped X_train from (1395 X 49) to (1395 X 49 X 1) as Keras-LSTM require 3-D Input
X_train = np.array(X_train).reshape((X_train.shape[0], X_train.shape[1], 1))
X_test = np.array(X_test).reshape((X_test.shape[0], X_test.shape[1], 1))

# Convert int-labels to One-hot-Labels for inputting to model later.
y_data = np.concatenate((y_train, y_test))
y_data = to_categorical(y_data) 

# Generate train and test one-hot-labels
y_train = y_data[:1395]
y_test = y_data[1395:]

# Converting int values to float for enabling matrix multiplications in model.
X_train = X_train.astype('float32') 

# Defining the Model:
def bilstm():
    model = Sequential()
    
    # With return_sequence=TRUE, the output will be a sequence of same length as input, with FALSE, output will be just one vector.
    # Input Shape = (49 X 1) as Keras-LSTM by-default needs 3D input, and 2D input in one Input-Sample. 
    model.add(Bidirectional(LSTM(50, input_shape = (49,1), return_sequences = False)))

    # input_dim : Size of the vocabulary
    # output_dim : Length of the vector for each word
    # input_length : Maximum length of a sequence
    model.add(Embedding(20000, 128, input_shape = (49,1))) 
    model.add(Bidirectional(LSTM(50)))

    model.add(Dense(46))
    model.add(Activation('softmax'))
    adam = optimizers.Adam(lr = 0.001)
    model.compile(loss = 'categorical_crossentropy', optimizer = adam, metrics = ['accuracy'])
    return model

# Building and training Model:
model = KerasClassifier(build_fn = bilstm, epochs = 200, batch_size = 50, verbose = 1)
model.fit(X_train, y_train)

# now predicting model's output accuracy:
# y_pred = model.predict(X_test)
# y_test_ = np.argmax(y_test, axis = 1)
# print(accuracy_score(y_pred, y_test_))
