# code for Glove word embedding
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
  
x = {'went', 'to', 'river', 'bank', 'with', 'power', 'bank'}
  
# create the dict.
tokenizer = Tokenizer()
tokenizer.fit_on_texts(x)
  
# number of unique words in dict.
print("Number of unique words in dictionary=", len(tokenizer.word_index))
print("Dictionary is = ", tokenizer.word_index)
  
# download glove and unzip it in Notebook.
#!wget http://nlp.stanford.edu/data/glove.6B.zip
#!unzip glove*.zip
  
# vocab: 'the': 1, mapping of words with
# integers in seq. 1,2,3..
# embedding: 1->dense vector
def embedding_for_vocab(filepath, word_index,
                        embedding_dim):
    vocab_size = len(word_index) + 1
      
    # Adding again 1 because of reserved 0 index
    embedding_matrix_vocab = np.zeros((vocab_size,
                                       embedding_dim))
  
    with open(filepath, encoding="utf8") as f:
        for line in f:
            word, *vector = line.split()
            if word in word_index:
                idx = word_index[word]
                embedding_matrix_vocab[idx] = np.array(vector, dtype=np.float32)[:embedding_dim]
                
    return embedding_matrix_vocab
  
  
# matrix for vocab: word_index
embedding_dim = 50
embedding_matrix_vocab = embedding_for_vocab('./glove.6B.50d.txt', tokenizer.word_index, embedding_dim)
print("Dense vector for first word is => ",embedding_matrix_vocab[1])



#####################################################################################################
# Since (idx == 0) was dummy point in the embedding_vocab_matrix, we will remove it while plotting.
embedding_matrix_vocab = embedding_matrix_vocab[1:]
# Now we are generating word-list for labelling points in the graph:
word_list = []
index_to_word = {}
for key, value in tokenizer.word_index.items():
    index_to_word[value] = key
for i in range(1 , len(index_to_word) + 1):
    word_list.append(index_to_word[i])
#####################################################################################################
# Now using PCA to reduce dimensionality to 2, for plotting the points:
from sklearn.decomposition import PCA
from matplotlib import pyplot

X = embedding_matrix_vocab
pca = PCA(n_components=2)
result = pca.fit_transform(X)

# create a scatter plot of the projection
pyplot.scatter(result[:, 0], result[:, 1])
words = word_list
for i, word in enumerate(words):
	pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
pyplot.show()
