import spacy
nlp = spacy.load('en_core_web_md')
# Simiarity score are better with 'md' than with 'sm'
token1 = nlp('cat')
token2 = nlp('dog')
  
print("Similarity:", token1.similarity(token2))