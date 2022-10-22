import nltk
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize
text = word_tokenize("I want an early upgrade")
nltk.pos_tag(text)
