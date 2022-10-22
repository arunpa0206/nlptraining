import spacy
nlp = spacy.load('en_core_web_md')

token1 = nlp('cat')
token2 = nlp('dog')
  
print("Similarity:", token1.similarity(token2))