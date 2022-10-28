import nltk
nltk.download('reuters')
from nltk.corpus import reuters

sents1 = reuters.sents()

sents2  = [['Ram', 'likes', 'this', 'book'], ['This', 'is', 'my', 'pen'], ['This', 'is', 'my', 'copy']]

sents = sents2

