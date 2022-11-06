import nltk
import string
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.util import ngrams
nltk.download('stopwords')

# write the removal characters such as : Stopwords and punctuation
def getRemovalList():
    # get all the English stop words
    stop_words = set(stopwords.words('english'))
    # get all the puncutations that we want to have in removal list
    string.punctuation = string.punctuation +'"'+'"'+'-'+'''+'''+'—'
    #adding stopwords and punctuations to make a removal list
    removal_list = list(stop_words) + list(string.punctuation)+ ['lt','rt']
    return(removal_list)

# convert upper case letters to lower case in a sentence
def get_lower_sentences(sentence):
    sentence = list(map(lambda x:x.lower(),sentence))
    return sentence

# get unigrams from a sentence
def get_unigram(sentence, unigram):
    for word in sentence:
        if word== '.':
            sentence.remove(word) 
        else:
            unigram.append(word)

    return unigram

# get bigrams from a sentence
def get_bigram(sentence, bigram):
    bigram.extend(list(ngrams(sentence, 2,pad_left=True, pad_right=True)))
    return bigram

# get trigrams from a sentence
def get_trigram(sentence, trigram):
    trigram.extend(list(ngrams(sentence, 3, pad_left=True, pad_right=True)))
    return trigram

# generate unigrams bigrams trigrams
def get_ngrams(sents):
    unigram=[]
    bigram=[]
    trigram=[]
    
    for sentence in sents:
        sentence = get_lower_sentences(sentence)
        
        unigram = get_unigram(sentence, unigram)
        bigram = get_bigram(sentence, bigram)
        trigram = get_trigram(sentence, trigram)

    return unigram, bigram, trigram

# remove the n-grams with removable words
def filter_stopwords(ngrams, removal_list):     
    filtered_ngrams = []

    # iterate over all the ngrams
    for ngram in ngrams:
        count = 0

        # iterate over each ngram
        for word in ngram:
            if word not in removal_list:
                count = 1
        if (count==1):
            filtered_ngrams.append(ngram)
    return (filtered_ngrams)

#input sentences are processed and stopwords are removed and also generates frequency distribution of n-grams
def text_processing(sents):
    
    removal_list = getRemovalList()

    unigram, bigram, trigram = get_ngrams(sents)
    
    unigram = filter_stopwords(unigram, removal_list)
    bigram = filter_stopwords(bigram, removal_list)
    trigram = filter_stopwords(trigram, removal_list)

    # generate frequency of n-grams 
    freq_ui = FreqDist(unigram)
    freq_bi = FreqDist(bigram)
    freq_tri = FreqDist(trigram)

    return freq_ui, freq_bi, freq_tri