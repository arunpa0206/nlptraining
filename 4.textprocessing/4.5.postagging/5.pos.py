import nltk
# averaged_perceptron_tagger is a nltk library used for tagging tokens to thier POS.
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize
text = word_tokenize("I want an early upgrade")
output_txt = nltk.pos_tag(text)
print(output_txt)
