from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
 #NLTK portal stemming algorrithm removes suffixes 
ps = PorterStemmer()
words = ["program", "programs", "programmer", "programming"]
  
for w in words:
    print(w, "->", ps.stem(w) + " | " , end = " ")