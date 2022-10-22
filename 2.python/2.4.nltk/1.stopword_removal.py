from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
  
input_txt = "Please give me your hand. I need to check it for any injuries."

stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(input_txt)
output_txt = [w for w in word_tokens if not w.lower() in stop_words]
  
print(word_tokens)
print(output_txt)