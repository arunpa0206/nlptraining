# zipfs law
import re
  
frequency = {}
 
with open('/content/drive/MyDrive/pg345.txt', 'r') as content:
    text_string = content.read()
 
    words = re.findall(r'\b[A-Za-z][a-z]{2,9}\b', text_string)
         
    for word in words:
        count = frequency.get(word,0)
        frequency[word] = count + 1
 
    most_frequent = dict(sorted(frequency.items(), key=lambda elem: elem[1], reverse=True))

    top_count = 0
         
    for idx, (words, frequency) in enumerate(most_frequent.items()):
        if(idx==0):
          top_count = frequency
        print(words, frequency, round(top_count/frequency, 2))
        if(idx==10):
          break
