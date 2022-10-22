from nltk.stem import WordNetLemmatizer
  
lemmatizer = WordNetLemmatizer()
  
print("caring :", lemmatizer.lemmatize("caring"))
print("care :", lemmatizer.lemmatize("care"))
print("cared :", lemmatizer.lemmatize("cared"))
print("cares :", lemmatizer.lemmatize("cares"))
print("cars :", lemmatizer.lemmatize("cars"))
  
# a denotes adjective in "pos"
print("better :", lemmatizer.lemmatize("better", pos ="a"))
