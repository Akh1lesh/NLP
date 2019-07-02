from bs4 import BeautifulSoup
from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize 
#from nltk.corpus import brown
from nltk.tokenize import word_tokenize
import urllib 

# response = urllib.urlopen('http://php.net/') 

# html = response.read() 

# soup = BeautifulSoup(html,"html5lib") 
# text = soup.get_text(strip=True) 
# text = "Akhilesh Mehar is is is the the best"
# tokens = word_tokenize(text)
mytext = "Hello Adam, how are you? I hope everything is going well. Today is a good day, see you dude." 

print(word_tokenize(mytext))
# freq = FreqDist(tokens) 

# for key,val in freq.items(): 

#     print (str(key) + ':' + str(val))
