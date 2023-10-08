from bs4 import BeautifulSoup
import requests


#Page to scrape from
page_to_scrape = requests.get('https://quotes.toscrape.com/')

soup = BeautifulSoup(page_to_scrape.text, "html.parser")
#Store all attributes with the span class = text
quotes = soup.findAll("span", attrs = {"class": "text"})
#Store all attributes with the small class = author
author = soup.findAll("small", attrs = {"class": "author"})

#Prints the list of quotes with authors
for x,y in zip(quotes,author):
    print(x.text + "  -  " + y.text)

