import nltk
import string
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.util import ngrams
nltk.download('stopwords')

#input sentences are processed and stopwords are removed and also generates frequency distribution of n-grams
def text_processing(sents):
    # write the removal characters such as : Stopwords and punctuation
    def getRemovalList():
        stop_words = set(stopwords.words('english'))
        string.punctuation = string.punctuation +'"'+'"'+'-'+'''+'''+'—'
        removal_list = list(stop_words) + list(string.punctuation)+ ['lt','rt']
        return(removal_list)

    # generate unigrams bigrams trigrams
    def get_ngrams(sents):
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
    
    removal_list = getRemovalList()

    unigram, bigram, trigram, tokenized_text = get_ngrams(sents)
    
    unigram = filter_stopwords(unigram)
    bigram = filter_stopwords(bigram)
    trigram = filter_stopwords(trigram)

    # generate frequency of n-grams 
    freq_ui = FreqDist(unigram)
    freq_bi = FreqDist(bigram)
    freq_tri = FreqDist(trigram)

    return freq_ui, freq_bi, freq_tri