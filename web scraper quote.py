from bs4 import BeautifulSoup
import requests
import re


my_url = 'https://www.brainyquote.com/topics/motivational'

source = requests.get(my_url).text

# Gets source text (HTML) of the url

soup = BeautifulSoup(source, 'lxml')

#Parses HTML


regex_quote = re.compile('.*b-qt*.')
regex_author = re.compile('.*b-aut*.')

quotes = soup.findAll('a', class_ = regex_quote)
authors = soup.findAll('a', class_ = regex_author)

i = 0

for i in range (0,len(quotes)):
    quote = quotes[i].text
    print()
    print(quote)
    i += 1


#puthor = soup.find('a', class_ = 'bq-aut qa_410518 oncl_a').text


#Want to find_all where class_ = contains"b-qt" for quotes



#print()
#print(author)
