import spacy
 
nlp = spacy.load('en_core_web_sm')
doc = nlp('programs programming programmer')
 
for token in doc:
    print(token.text + " -> " + token.lemma_ + " | ", end = " " )