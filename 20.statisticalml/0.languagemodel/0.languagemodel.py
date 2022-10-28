# imports
from pipeline import sents
from textprocessing import text_processing

freq_ui, freq_bi, freq_tri = text_processing(sents)
  
#calculating probability 
def get_prob(word1, word2, curr_word, freq_ui, freq_bi, freq_tri):
  if(freq_bi[word1, word2]==0):
    return 0
  prob_val = freq_tri[word1, word2, curr_word]/freq_bi[word1, word2]
  return prob_val

#predicting next word
def predict_next_word(word1, word2, s):
  for i in range(5):
      max_count = 0
      next_word = ""
      for curr_word in freq_ui:
        prob_val = get_prob(word1, word2, curr_word, freq_ui, freq_bi, freq_tri)
        if(prob_val > max_count):
          max_count = prob_val
          next_word = curr_word
      
      s=s+' '+ next_word
      print(s)
      word1 = word2
      word2 = next_word

# Next word prediction      
word1 = "he"
word2 = "said"

s = word1 + ' ' + word2
print(s)

predict_next_word(word1, word2, s)
