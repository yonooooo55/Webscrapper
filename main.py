import csv

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
#for q,a in zip(quotes,author):
    #print(q.text + "  -  " + a.text)

csvCount = 1
file = open ("Webscraping_%d.csv"%csvCount, "w", newline="")
writer = csv.writer(file)
csvCount += 1

#Sets up the headers in the excel file
writer.writerow(["QUOTES", "AUTHORS"])



for q,a in zip(quotes,author):
    print(q.text + " - " + a.text)
    #Insert into each row
    writer.writerow([q.text, a.text])


file.close()