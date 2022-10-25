import pandas as pd
import matplotlib.pyplot as plt

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM,Dense, Dropout, SpatialDropout1D
from tensorflow.keras.layers import Embedding
#load the csv file into the dataframe
df = pd.read_csv("Tweets.csv")
#pick the text and airline sentiment
tweet_df = df[['text','airline_sentiment']]
#Pick rows with sentiment not nuetral
tweet_df = tweet_df[tweet_df['airline_sentiment'] != 'neutral']
#factorize method generates a numerical value for each catagory
sentiment_label = tweet_df.airline_sentiment.factorize()
#tokenize the tweets
tweet = tweet_df.text.values
tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(tweet)
#vocabolary size is the number of tokens
vocab_size = len(tokenizer.word_index) + 1
#transform each text to sequence of integers
encoded_docs = tokenizer.texts_to_sequences(tweet)
#Every ttweet is padded to have a total length of 200
padded_sequence = pad_sequences(encoded_docs, maxlen=200)
#create embedded vecttor length of 32 
embedding_vector_length = 32
model = Sequential()
#Use the input length of padded length 200 to form vectors for each word in the vocalobary 
model.add(Embedding(vocab_size, embedding_vector_length, input_length=200) )
#25 percent drop out reduces overfitting
model.add(SpatialDropout1D(0.25))

#add lstm layer of 50 lstm cells with a 50 percent drop out
model.add(LSTM(50, dropout=0.5, recurrent_dropout=0.5))
model.add(Dropout(0.2))
#add a fully connected layer
model.add(Dense(1, activation='sigmoid')) 
model.compile(loss='binary_crossentropy',optimizer='adam', metrics=['accuracy'])  
print(model.summary()) 
#get accuracy for 5 epochs with batch size of32
history = model.fit(padded_sequence,sentiment_label[0],validation_split=0.2, epochs=5, batch_size=32)
#Plot graph for validation accuracy vs epochs
plt.plot(history.history['accuracy'], label='acc')
plt.plot(history.history['val_accuracy'], label='val_acc')
plt.legend()
plt.show()
plt.savefig("Accuracy plot.jpg")

plt.plot(history.history['loss'], label='loss')
plt.plot(history.history['val_loss'], label='val_loss')
plt.legend()
plt.show()
plt.savefig("Loss plot.jpg")
#Predict sentiment for the given sentence
def predict_sentiment(text):
    tw = tokenizer.texts_to_sequences([text])
    tw = pad_sequences(tw,maxlen=200)
    prediction = int(model.predict(tw).round().item())
    print("Predicted label: ", sentiment_label[1][prediction])
    
test_sentence1 = "This is good"
predict_sentiment(test_sentence1)

test_sentence2 = "This is the worst flight experience of my life!"
predict_sentiment(test_sentence2)
