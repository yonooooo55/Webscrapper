# Web Scraping Project

A simple web scraping project to learn the basics of web scraping using Python.

## Technologies Used
- Python
- BeautifulSoup
- Requests

## How to Use
1. Clone the repository: `git clone https://github.com/your-username/your-repo.git`
2. Run from venv

## Code Examples
```python
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
