from gensim.models import Word2Vec
import numpy as np

sen1 = ['president', 'greets', 'press', 'chicago']
sen2 = ['obama', 'speaks', 'illinois']
sentences = [sen1, sen2]
model = Word2Vec(sentences, min_count=1)

vec1 = np.zeros(100, dtype = 'float32')
vec2 = np.zeros(100, dtype = 'float32')

for word in sen1:
    arr = model.wv[word]
    vec1 = np.add(vec1,arr)
    
for word in sen2:
    arr = model.wv[word]
    vec2 = np.add(vec2,arr)
    
# Now we find cosine-similarity between these two vectors:
vec1 = vec1/len(sen1)
vec2 = vec2/len(sen2)

def CosineSimilarity(vA, vB):

    print("First-vector :  " + str(vA))  
    print("Second-vector :  " + str(vB))
    print('-----------------------------------------------')

    cos_sim = numpy.dot(vA, vB) / (numpy.sqrt(numpy.dot(vA,vA)) * numpy.sqrt(numpy.dot(vB,vB)))
    return cos_sim

print(CosineSimilarity(vec1,vec2))
