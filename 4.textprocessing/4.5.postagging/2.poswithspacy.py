import spacy

nlp = spacy.load("en_core_web_sm")
text = """I want an early upgrade"""
#spacy nlp object holds an array of token structures
#nlp(spacy-object) is a text processing pipeline offered by spacy
doc = nlp(text)

for token in doc:
    print(token, token.pos_)
