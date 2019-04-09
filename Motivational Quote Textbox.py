from bs4 import BeautifulSoup
import requests
import re
from tkinter import messagebox
import random

my_url = 'https://www.brainyquote.com/topics/motivational'

source = requests.get(my_url, verify = True).text

soup = BeautifulSoup(source, 'lxml')

print(soup.prettify())

regex_quote = re.compile('.*b-qt*.')
regex_author = re.compile('.*bq-aut*.')

quotes = soup.findAll('a', class_ = regex_quote)
authors = soup.findAll('a', class_ = regex_author)

n = random.randint(0,len(quotes)-1)

messagebox.showinfo(authors[n].text,quotes[n].text)


    
