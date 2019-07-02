from bs4 import BeautifulSoup

import urllib

response = urllib.urlopen('http://php.net/') 

html = response.read()

soup = BeautifulSoup(html,"html5lib")

text = soup.get_text(strip=True)

print (text)