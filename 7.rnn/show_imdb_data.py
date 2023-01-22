from keras.datasets import imdb
max_features = 20000
print('Loading data...')
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)

# Printing first 5 data entries from imdb dataset:
for i in range(5):
    print(x_train[i])
    print('-----------------------------------------------------------')