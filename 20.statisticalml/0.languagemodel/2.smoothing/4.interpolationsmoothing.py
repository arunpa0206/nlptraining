# Next word prediction     
# Interpolation Smoothing

from textprocessing import freq_ui, freq_bi, freq_tri

def get_prob_by_applying_interpolation_smoothing(word1, word2, curr_word, freq_ui, freq_bi, freq_tri):
  lambda1 = 1/3.0
  lambda2 = 1/3.0
  lambda3 = 1/3.0

  if(freq_ui[word2]==0):
      lambda2 = 0
      freq_ui[word2] = 1
  if(freq_bi[word1, word2]==0):
      lambda3 = 0
      freq_bi[word1, word2] = 1
        
  prob_val = (lambda1 * (freq_ui[curr_word]/6)) + (lambda2 * (freq_bi[word2, curr_word]/freq_ui[word2])) + (lambda3 * (freq_tri[word1, word2, curr_word]/freq_bi[word1, word2])) 
  return prob_val

def predict_next_word(word1, word2, s):
  for i in range(2):
      max_count = 0
      next_word = ""
      for curr_word in freq_ui:

        prob_val = get_prob_by_applying_interpolation_smoothing(word1, word2, curr_word, freq_ui, freq_bi, freq_tri)

        if(prob_val > max_count):
          max_count = prob_val
          next_word = curr_word
      
      s=s+' '+ next_word
      print(s)
      word1 = word2
      word2 = next_word

word1 = "Mukesh"
word2 = "likes"

s = word1 + ' ' + word2
print(s)

predict_next_word(word1, word2, s)
