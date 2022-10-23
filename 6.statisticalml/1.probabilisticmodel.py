# Probabilistic Modeling


bigram1 = {'Let' : {'the': 0.2857142857142857, 'dainty':
0.14285714285714285, 'it': 0.14285714285714285, 'those':
0.14285714285714285, 'me': 0.14285714285714285, 'us':
0.14285714285714285}}

bigram2 = {'the' : {'dogs' : 0.4, 'it' : 0.2, 'a' : 0.2, 'b': 0.2}}
bigram3 = {'dogs' : {'out' : 0.6, 'it' : 0.2, 'jj' : 0.2}}

model = {}
model.update(bigram1)
model.update(bigram2)
model.update(bigram3)

sentence = []

iterations = 3
word = 'Let'
sentence.append(word)

for _ in range(iterations):
    max_value = 0
    for k, v in model[word].items():
        if v >= max_value:
            word = k
            max_value = v
    sentence.append(word)


print(" ".join(sentence)) 
