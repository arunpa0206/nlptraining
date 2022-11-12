# Next word prediction     
# Add-k smoothing

from textprocessing import text_processing
sents  = [['Ram', 'likes', 'this', 'book'], ['This', 'is', 'my', 'pen'], ['This', 'is', 'my', 'copy']]
freq_ui, freq_bi, freq_tri = text_processing(sents)

#calculate probability using add-k smoothing
def get_prob_by_applying_addk_smoothing(word1, word2, curr_word, freq_ui, freq_bi, freq_tri):
  prob_val = (freq_tri[word1, word2, curr_word]+0.5)/(freq_bi[word1, word2]+6)
  return prob_val

#predicting next word
def predict_next_word(word1, word2, s):
  for i in range(1):
      max_count = 0
      next_word = ""
      for curr_word in freq_ui:
        
        prob_val = get_prob_by_applying_addk_smoothing(word1, word2, curr_word, freq_ui, freq_bi, freq_tri)
        if(prob_val > max_count):
          max_count = prob_val
          next_word = curr_word
      
      s=s+' '+ next_word
      print(s)
      word1 = word2
      word2 = next_word

word1 = "ram"
word2 = "plays"

s = word1 + ' ' + word2
print(s)

predict_next_word(word1, word2, s)
