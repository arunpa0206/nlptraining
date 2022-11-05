import spacy
from spacy import displacy

NER = spacy.load("en_core_web_sm")

input_txt = "Apple today announced second generation Iphone"

output = NER(input_txt)

for word in output.ents:
    print(word.text +  " -> " + word.label_)
#spacy version 3.1.2 appears to give better results