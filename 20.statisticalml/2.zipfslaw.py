# zipfs law- demonstration of the distribution of zipfs law frequency ratios
import re
#Creating a frequency dictionary for each word frequency mapping 
frequency = {}
 #read the contents of the file and store in the string
with open('pg345.txt', 'r') as content:
    text_string = content.read()
    #find all the words that have capital letter to start followed by small letters  with 2 to 9 letters
    words = re.findall(r'\b[A-Za-z][a-z]{2,9}\b', text_string)
    #increment the frequency of the word if it exists otherwise increment to 1   
    for word in words:
        count = frequency.get(word,0)
        frequency[word] = count + 1
    #sorting the dictionary using lambda function
    most_frequent = dict(sorted(frequency.items(), key=lambda elem: elem[1], reverse=True))
    #this variable maintains the frequency of the most occuring word in the corpus
    top_count = 0
    #frequency ratio of the most occuring word to other words will be equal to the rank approximately.    
    for idx, (words, frequency) in enumerate(most_frequent.items()):
        if(idx==0):
          top_count = frequency
        print(words, frequency, round(top_count/frequency, 2))
        if(idx==10):
          break
