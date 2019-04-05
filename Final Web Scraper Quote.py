from bs4 import BeautifulSoup
import requests
import re


my_url = 'https://www.brainyquote.com/topics/motivational'

source = requests.get(my_url).text

# Gets source text (HTML) of the url

soup = BeautifulSoup(source, 'lxml')

#Parses HTML

regex_quote = re.compile('.*b-qt*.')
regex_author = re.compile('.*bq-aut*.')

quotes = soup.findAll('a', class_ = regex_quote)
authors = soup.findAll('a', class_ = regex_author)

i = 0

for i in range (0,len(quotes)):
    quote = quotes[i].text
    author = authors[i].text
    print()
    print(quote)
    print()
    print('-' + str(author))
    i += 1
