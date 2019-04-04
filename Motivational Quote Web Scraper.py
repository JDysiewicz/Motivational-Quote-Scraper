from bs4 import BeautifulSoup
import requests


my_url = 'https://www.brainyquote.com/topics/motivational'

source = requests.get(my_url).text

# Gets source text (HTML) of the url

soup = BeautifulSoup(source, 'lxml')

#Parses HTML




quote = soup.find('a', class_ = "b-qt qt_410518 oncl_q").text
#puthor = soup.find('a', class_ = 'bq-aut qa_410518 oncl_a').text


#Want to find_all where class_ = contains"b-qt" for quotes

print()
print(quote)


#print()
#print(author)