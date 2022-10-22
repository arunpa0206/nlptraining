from gensim.models import Word2Vec
# define tokenized training data
sentences = [['went'],['to'],['river'],['bank'],['with'],['power'],['bank']]

model = Word2Vec(sentences, min_count=1)
words = list(model.wv.index_to_key)
print(model.wv['bank'])