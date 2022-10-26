# imports
import string
import random
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('reuters')
from nltk.corpus import reuters
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.util import ngrams
from collections import defaultdict
from collections import Counter
# input the reuters sentences
sents = reuters.sents()
  
# write the removal characters such as : Stopwords and punctuation
def getRemovalList():
  stop_words = set(stopwords.words('english'))
  string.punctuation = string.punctuation +'"'+'"'+'-'+'''+'''+'—'
  removal_list = list(stop_words) + list(string.punctuation)+ ['lt','rt']
  return(removal_list)
  
removal_list = getRemovalList()


# generate unigrams bigrams trigrams
def get_Unigrams(sents):
  unigram=[]
  bigram=[]
  trigram=[]
  tokenized_text=[]
  for sentence in sents:
    sentence = list(map(lambda x:x.lower(),sentence))
    
    for word in sentence:
          if word== '.':
              sentence.remove(word) 
          else:
              unigram.append(word)
      
    tokenized_text.append(sentence)
    bigram.extend(list(ngrams(sentence, 2,pad_left=True, pad_right=True)))
    trigram.extend(list(ngrams(sentence, 3, pad_left=True, pad_right=True)))

  return unigram, bigram, trigram, tokenized_text

unigram, bigram, trigram, tokenized_text = get_Unigrams(sents)
  
# remove the n-grams with removable words
def filter_stopwords(x):     
    y = []
    for pair in x:
        count = 0
        for word in pair:
            if word in removal_list:
                count = count or 0
            else:
                count = count or 1
        if (count==1):
            y.append(pair)
    return (y)
unigram = filter_stopwords(unigram)
bigram = filter_stopwords(bigram)
trigram = filter_stopwords(trigram)

# generate frequency of n-grams 
freq_ui = FreqDist(unigram)
freq_bi = FreqDist(bigram)
freq_tri = FreqDist(trigram)

# Next word prediction      
word1 = "he"
word2 = "said"

s = word1 + ' ' + word2
print(s)

def get_prob(word1, word2, curr_word, freq_ui, freq_bi, freq_tri):
  if(freq_bi[word1, word2]==0):
    return 0
  prob_val = freq_tri[word1, word2, curr_word]/freq_bi[word1, word2]
  return prob_val

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

predict_next_word(word1, word2, s)
