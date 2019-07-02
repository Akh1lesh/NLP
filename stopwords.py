from bs4 import BeautifulSoup
from nltk.probability import FreqDist
#from nltk.corpus import brown
from nltk.tokenize import word_tokenize
import urllib 

# response = urllib.urlopen('http://php.net/') 

# html = response.read() 

# soup = BeautifulSoup(html,"html5lib") 
# text = soup.get_text(strip=True) 
text = "Akhilesh Mehar is is the the best"
tokens = word_tokenize(text)
freq = FreqDist(tokens) 

for key,val in freq.items(): 

    print (str(key) + ':' + str(val))
from bs4 import BeautifulSoup
from nltk.probability import FreqDist
#from nltk.corpus import brown
from nltk.tokenize import word_tokenize
import urllib 

# response = urllib.urlopen('http://php.net/') 

# html = response.read() 

# soup = BeautifulSoup(html,"html5lib") 
# text = soup.get_text(strip=True) 
text = "Akhilesh Mehar is is is the the best"
tokens = word_tokenize(text)
# freq = FreqDist(tokens)
clean_tokens = tokens[:] 

sr = stopwords.words('english') 

for token in tokens: 

    if token in stopwords.words('english'): 

        clean_tokens.remove(token) 

freq = nltk.FreqDist(clean_tokens)  

for key,val in freq.items(): 

    print (str(key) + ':' + str(val))
freq.plot(20,cumulative=False)