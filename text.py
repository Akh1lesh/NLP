import urllib

response = urllib.urlopen('http://php.net/')

html = response.read()

print (html)