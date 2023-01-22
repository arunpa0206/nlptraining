from keras.datasets import reuters
num_words = 30000
maxlen = 50
test_split = 0.3
(X_train, y_train), (X_test, y_test) = reuters.load_data(num_words = num_words, maxlen = maxlen, test_split = test_split)
X_train = pad_sequences(X_train, padding = 'post')

for i in range(5):
    print(X_train[i])
    print('-----------------------------------------------------------')