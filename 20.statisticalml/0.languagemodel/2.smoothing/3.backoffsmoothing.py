# Next word prediction     
# Backoff Smoothing

from textprocessing import freq_ui, freq_bi, freq_tri

word1 = "shyam"
word2 = "likes"

s = word1 + ' ' + word2
print(s)

def get_prob_by_applying_backoff_smoothing(word1, word2, curr_word, freq_ui, freq_bi, freq_tri):
  if(freq_ui[word2]==0):
    return 0
  prob_val = (freq_bi[word2, curr_word])/(freq_ui[word2])
  return prob_val

def predict_next_word(word1, word2, s):
  for i in range(1):
      max_count = 0
      next_word = ""
      for curr_word in freq_ui:
        
        prob_val = get_prob_by_applying_backoff_smoothing(word1, word2, curr_word, freq_ui, freq_bi, freq_tri)
        if(prob_val > max_count):
          max_count = prob_val
          next_word = curr_word
      
      s=s+' '+ next_word
      print(s)
      word1 = word2
      word2 = next_word

predict_next_word(word1, word2, s)
