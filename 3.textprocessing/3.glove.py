from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
  
x = ['went', 'to', 'river', 'bank', 'with', 'power', 'bank']

tokenizer = Tokenizer()
tokenizer.fit_on_texts(x)
print("Number of unique words in dictionary=", len(tokenizer.word_index))
print("Dictionary is = ", tokenizer.word_index)

#!wget http://nlp.stanford.edu/data/glove.6B.zip
def embedding_for_vocab(filepath, word_index,embedding_dim):
    vocab_size = len(word_index) + 1
      
    # Adding again 1 because of reserved 0 index
    embedding_matrix_vocab = np.zeros((vocab_size, embedding_dim))
  
    with open(filepath, encoding="utf8") as f:
        for line in f:
            word, *vector = line.split()
            if word in word_index:
                idx = word_index[word]
                embedding_matrix_vocab[idx] = np.array(
                    vector, dtype=np.float32)[:embedding_dim]
  
    return embedding_matrix_vocab
  
  
# matrix for vocab: word_index
embedding_dim = 50
embedding_matrix_vocab = embedding_for_vocab('glove.6B.50d.txt', tokenizer.word_index,embedding_dim)
print("Dense vector for first word is => ",embedding_matrix_vocab[1])