import spacy
 #English core 'sm' represents the small model trained by spacy for english
nlp = spacy.load('en_core_web_sm')
doc = nlp('care caring cares cared cars')
 
for token in doc:
    print(token.text + " -> " + token.lemma_ + " | ", end = " " )