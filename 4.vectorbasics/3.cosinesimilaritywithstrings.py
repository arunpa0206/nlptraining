A = "I love data mining"
B = "I hate data mining"

import numpy

wordsA = A.lower().split()
wordsB = B.lower().split()

print("Sent-1   :  " + str(wordsA))
print("Sent-2   :  " + str(wordsB))

vocab = set(wordsA)
vocab = vocab.union(set(wordsB))
vocab = list(vocab)

print("Vocab    :  " + str(vocab))


vA = numpy.zeros(len(vocab), dtype=float)
vB = numpy.zeros(len(vocab), dtype=float)

for w in wordsA:
    i = vocab.index(w)
    vA[i] += 1
    
print("Vector-1 :  " + str(vA))

for w in wordsB:
    i = vocab.index(w)
    vB[i] += 1
    
print("Vector-2 :  " + str(vB))


cos_sim = numpy.dot(vA, vB) / (numpy.sqrt(numpy.dot(vA,vA)) * numpy.sqrt(numpy.dot(vB,vB)))



print("\nCosine-Similarity : " + str(cos_sim))
