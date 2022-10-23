import nltk
from nltk.stem.snowball import SnowballStemmer
#Use uses snow ball stemmer which is a better variant of porter stemmer
#Try words like 'fairly' and 'sportingly'
snow_stemmer = SnowballStemmer(language='english')

words = ['care', 'caring', 'cares', 'cared', 'cars']
stem_words = []

for w in words:
    x = snow_stemmer.stem(w)
    stem_words.append(x)

for e1,e2 in zip(words,stem_words):
    print(e1+' ----> '+e2)
