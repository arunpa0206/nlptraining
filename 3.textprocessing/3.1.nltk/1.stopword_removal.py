#importing delauft stopwords from nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
  
input_txt = "Please give me your hand. I need to check it for any injuries."
#importing stop words of english that need to be filtered. We can also extend this list with our own list 
stop_words = set(stopwords.words('english'))
#Tokenize the input text
word_tokens = word_tokenize(input_txt)
#filter the stop words from the word tokens
output_txt = [w for w in word_tokens if not w.lower() in stop_words]
#print the tokenized input tokens 
print("Tokenized sentence:")
print(word_tokens)
#print the filtered tokens
print("Filtered Sentence:")
print(output_txt)