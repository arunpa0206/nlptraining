import spacy
from spacy import displacy

NER = spacy.load("en_core_web_sm")

input_txt = "Apple today announced second generation Iphone"

text1= NER(input_txt)

for word in text1.ents:
    print(word.text +  " -> " + word.label_ + " | ", end =" ")
