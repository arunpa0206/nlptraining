import torch
from pytorch_transformers import BertTokenizer
from pytorch_transformers import BertModel

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')
input_ids = torch.tensor(tokenizer.encode("went river bank with power bank")).unsqueeze(0)  # Batch size 1
outputs = model(input_ids)
# The last hidden-state is the first element of the output tuple
last_hidden_states = outputs[0]  

# Total number of word embeddings
print(len(last_hidden_states[0]))
# Printing 2nd word's embedding
print("'bank' in river bank" + str(last_hidden_states[0][2])) # embedding for 'bank'
print("'bank' in power bank" + str(last_hidden_states[0][5])) # embedding for 'bank'

print("input ids : " + str(input_ids))

############################################################################
# Now using PCA to reduce dimensionality to 2, for plotting the points:
from sklearn.decomposition import PCA
from matplotlib import pyplot

# creates the last hidden state as a numpy matrix.
X = last_hidden_states[0].detach().numpy()
print(type(X))
pca = PCA(n_components=2)
result = pca.fit_transform(X)
# result will be a mtrix containing (no-of-words X 2){x and y coordinates of the PCA output}

# create a scatter plot of the projection
pyplot.scatter(result[:, 0], result[:, 1])
words = ['went', 'river', 'bank', 'with', 'power', 'bank']
for i, word in enumerate(words):
	pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
pyplot.show()
