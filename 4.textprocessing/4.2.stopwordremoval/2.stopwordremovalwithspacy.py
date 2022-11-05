from spacy.lang.en import English
from spacy.lang.en.stop_words import STOP_WORDS
#Create an English language centric nlp object
nlp = English()

text = "Please give me your hand. I need to check it for any injuries."

my_doc = nlp(text)
print(my_doc)

token_list = []
for token in my_doc:
    token_list.append(token.text)
    
filtered_sentence =[] 

for word in token_list:
    lexeme = nlp.vocab[word]
    # lexeme is a concept that can be represented by multiple words 
    if lexeme.is_stop == False:
        filtered_sentence.append(word) 
print("input sentence tokens:")        
print(token_list)
print("filtered tokens:")
print(filtered_sentence)  
