# LAB EXERCISE 05
import requests
from bs4 import BeautifulSoup

### SET UP BEGINS Do not modify
punctuations = ["—", "–", "-", ":"]

city_locations = [
    {"name": "Boston", "latitude": 42.36, "longitude": -71.06},
    {"name": "New York", "latitude": 40.71, "longitude": -74.01},
    {"name": "Fake City", "latitude": 999, "longitude": -999}
]
### SET UP ENDS Do not modify

# PROBLEM 01

def scrape_quotes_by_author(num_pages):
    """
    Scrape quotes from quotes.toscrape.com for pages 1 through num_pages and
    return a dictionary mapping each author's name (str) to a list of their
    quotes (list of str). Stops early if a page has no quotes.
    """
    quotes_by_author = {}
 
    for page in range(1, num_pages + 1):
        url = f"https://quotes.toscrape.com/page/{page}/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
 
        quote_blocks = soup.find_all("div", class_="quote")
        if not quote_blocks:
            # Past the last real page -> return what we have so far
            break
 
        for block in quote_blocks:
            text = block.find("span", class_="text").get_text().strip()
            author = block.find("small", class_="author").get_text().strip()
            quotes_by_author.setdefault(author, []).append(text)
 
    return quotes_by_author


# PROBLEM 02

# PROBLEM 03

def main():
    pass

if __name__ == '__main__':
    main()

