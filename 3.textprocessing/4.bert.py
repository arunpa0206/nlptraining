
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
print(last_hidden_states[0][2]) # embedding for 'bank'

print(input_ids)
