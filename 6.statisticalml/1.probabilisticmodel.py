# Probabilistic Modeling

#assuming that bigram was generated from a corpus of text
#p(the | let)
bigram1 = {'Let' : {'the': 0.2857142857142857, 'dainty':
0.14285714285714285, 'it': 0.14285714285714285, 'those':
0.14285714285714285, 'me': 0.14285714285714285, 'us':
0.14285714285714285}}
#p(dogs | the)
bigram2 = {'the' : {'dogs' : 0.4, 'it' : 0.2, 'a' : 0.2, 'b': 0.2}}
#p(out | dogs)
bigram3 = {'dogs' : {'out' : 0.6, 'it' : 0.2, 'jj' : 0.2}}
#model is a dictionary that contains bigrams
model = {}
model.update(bigram1)
model.update(bigram2)
model.update(bigram3)
#create a empty sentence to add generated words
sentence = []
#the sentence will have iterations+1 number of words
iterations = 3
#this will be the first word of the sentence
word = 'Let'
sentence.append(word)

for _ in range(iterations):
    #this variable is used to find the word with maximum probability
    max_value = 0
    for k, v in model[word].items():
        if v >= max_value:
            word = k
            max_value = v
    #add the word with maximum probability
    sentence.append(word)


print(" ".join(sentence)) 
