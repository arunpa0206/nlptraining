# Next word prediction     
# Backoff Smoothing

from textprocessing import freq_ui, freq_bi, freq_tri

word1 = "shyam"
word2 = "likes"

s = word1 + ' ' + word2
print(s)

def predict_next_word(word1, word2, s):
  for i in range(1):
      max_count = 0
      next_word = ""
      for curr_word in freq_ui:
        
        prob_val = (freq_bi[word2, curr_word])/(freq_ui[word2])
        if(prob_val > max_count):
          max_count = prob_val
          next_word = curr_word
      
      s=s+' '+ next_word
      print(s)
      word1 = word2
      word2 = next_word

predict_next_word(word1, word2, s)
