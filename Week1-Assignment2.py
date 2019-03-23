from cgitb import html
from urllib import request

import nltk
from bs4 import BeautifulSoup

url = "http://www.gutenberg.org/files/2554/2554-0.txt"
response = request.urlopen(url)
raw = response.read().decode("utf-8-sig")
raw.find("PART I")
raw.rfind("End of Project")
raw = raw[5335:1157809]
tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)
text.collocations()

raw = BeautifulSoup(html, "lxml").get_text()
print(raw)
