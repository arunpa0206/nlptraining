import keras
import numpy as numpy
from keras.datasets import reuters
# reuters is a news dataset collection of keras, which is classfied into 46 topics.


np_load_old = numpy.load
# modify the default parameters of np.load
#numpy.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)
#Using TensorFlow backend.


(x_train, y_train), (x_test, y_test) = reuters.load_data(num_words=None, test_split=0.2)
# setting 'num_words==0' means we are setting no cap on the no of words in the dataset. 
# If it was set to 100, then the 100 most frequenty used words in the dataset.
# Use 20% data as test-set.


word_index = reuters.get_word_index(path="reuters_word_index.json")
# We actually dont get words, we get word-indices. So this function is used to get the word-index relation.


num_classes = max(y_train) + 1
print('# of Training Samples: {}'.format(len(x_train)))
print('# of Test Samples: {}'.format(len(x_test)))
print('# of Classes: {}'.format(num_classes))
# of Training Samples: 8982
# of Test Samples: 2246
# of Classes: 46


# Here we are seeing the data in the datset:
# Seeing x_train[1] and y_train[1] as example here:
#####################################################################################################
print("Document-1 : \n" + str(x_train[1])) # Printing raw data from dataset.
print('------------------------------------------------------------')
# We have word-index dictionary, here we are reversing that dictionary to get index-word dictionary.
# This we do to see the data in the document, which is present in terms of indices.
index_to_word = {}
for key, value in word_index.items():
    index_to_word[value] = key
actual_doc = ' '.join([index_to_word[x] for x in x_train[1]])    
print("Document-1 : \n" + str(actual_doc))
print('------------------------------------------------------------')
print("\nNews Label Number for this Doc : " + str(y_train[1]))
#####################################################################################################

# we cap the maximum number of words in a news item to 10000 by specifying the 'max_words'
max_words = 10000

from keras.preprocessing.text import Tokenizer
tokenizer = Tokenizer(num_words=max_words)
x_train = tokenizer.sequences_to_matrix(x_train, mode='binary')
x_test = tokenizer.sequences_to_matrix(x_test, mode='binary')


# Using to_categorical, we transform both y_train and y_test into one-hot encoded vectors of length num_classes
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)
print("Output label converted to one-hot encoding vector for backpropagation step: \n")
print(y_train[1]) # one hot-vector for 1st document's output.
print(len(y_train[1])) # length of 1-hot-vector.



from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
model = Sequential() # Instantiate sequential model
model.add(Dense(512, input_shape=(max_words,)))  # 512 neurons in first layer, input shape = max_words, *(Anything can be expected)
model.add(Activation('relu'))  # Add second layer
model.add(Dropout(0.5)) # Add dropout layer = 50%, deavtivates the output of 50% of neurons from previous layer.
model.add(Dense(num_classes)) # Add fourth layer
model.add(Activation('softmax')) # Add Softmax layer
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# The loss function categorical crossentropy is used to quantify deep learning model errors, typically in single-label, multi-class classification problems
print(model.metrics_names)
# The attribute model.metrics_names will give you the display labels for the scalar outputs


batch_size = 32
epochs = 3
history = model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1, validation_split=0.1)
# 'verbose=1' -> Means training-progress-bar will be printed. 
# Validation-split -> separate a portion of your training data into a validation dataset and evaluate the performance of your model on that validation dataset in each epoch
# Validation split helps to improve the model performance by fine-tuning the model after each epoch.
score = model.evaluate(x_test, y_test, batch_size=batch_size, verbose=1)
# Performing Model Evaluation.

print('Test loss:', score[0])
print('Test accuracy:', score[1])
