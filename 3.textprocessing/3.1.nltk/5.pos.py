import nltk
#todoncomment
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize
text = word_tokenize("I want an early upgrade")
output_txt = nltk.pos_tag(text)
print(output_txt)
