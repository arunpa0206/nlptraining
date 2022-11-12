# Next word prediction     
# Backoff Smoothing

from textprocessing import text_processing
sents  = [['Ram', 'likes', 'this', 'book'], ['This', 'is', 'my', 'pen'], ['This', 'is', 'my', 'copy']]
freq_ui, freq_bi, freq_tri = text_processing(sents)

#calculate probability using backoff smoothing
def get_prob_by_applying_backoff_smoothing(word1, word2, curr_word, freq_ui, freq_bi, freq_tri):

  prob_val = 0

  # first we will try trigram
  if(freq_bi[word1, word2]!=0):
    prob_val = freq_tri[word1, word2, curr_word] / freq_bi[word1, word2]
  else:
    #then we will try bigram
    if(freq_ui[word2]!=0):
      prob_val = freq_bi[word2, curr_word] / freq_ui[word2]
    else:
      # then we will try unigram
      prob_val = freq_ui[curr_word] / 6
  
  return prob_val

#predicting next word
def predict_next_word(word1, word2, s):
  for i in range(2):
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

word1 = "shyam"
word2 = "likes"

s = word1 + ' ' + word2
print(s)

predict_next_word(word1, word2, s)
