from spacy.lang.en import English
from spacy.lang.en.stop_words import STOP_WORDS
nlp = English()

text = "Please give me your hand. I need to check it for any injuries."

my_doc = nlp(text)
token_list = []
for token in my_doc:
    token_list.append(token.text)
    
filtered_sentence =[] 

for word in token_list:
    lexeme = nlp.vocab[word]
    if lexeme.is_stop == False:
        filtered_sentence.append(word) 
        
print(token_list[0:8]) # Breaking in half for better visibility.
print(token_list[8:])
print()
print(filtered_sentence)  