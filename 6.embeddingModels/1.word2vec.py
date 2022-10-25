from gensim.models import Word2Vec
# define tokenized training data
# every word is mapped to an index and we use that index for training the model for that word
sentences = [['went'],['to'],['river'],['bank'],['with'],['power'],['bank']]

# min count represents the min no of words to be considered when training the model. Words with occurence less than this will be ignored.
model = Word2Vec(sentences, min_count=1)
words = list(model.wv.index_to_key)
print(words)
print(model.wv['bank'])
#######################################################
# Now using PCA to reduce dimensionality to 2, for plotting the points:
from sklearn.decomposition import PCA
from matplotlib import pyplot

X = model.wv[list(model.wv.index_to_key)]
pca = PCA(n_components=2)
result = pca.fit_transform(X)

# create a scatter plot of the projection
pyplot.scatter(result[:, 0], result[:, 1])
words = list(model.wv.index_to_key)
for i, word in enumerate(words):
	pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
pyplot.show()
