from gensim.models import Word2Vec
# define tokenized training data
# every word is mapped to an index and we use that index for training the model for that word
sentences = [['went'],['to'],['river'],['bank'],['with'],['power'],['bank']]

# min count represents the min no of words to be considered when training the model. Words with occurence less than this will be ignored.
model = Word2Vec(sentences, min_count=1)
words = list(model.wv.index_to_key)
print(words)
print(model.wv['bank'])