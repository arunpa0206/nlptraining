import spacy

nlp = spacy.load("en_core_web_sm")
text = """I want an early upgrade"""
doc = nlp(text)

for token in doc:
    print(token, token.pos_)
