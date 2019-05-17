from bs4 import BeautifulSoup
import requests
import re

class BasicScraper:
  def __init__(self, query):
    self.query = query.replace('+', ' ')
  
  def validate_title(self, title, found_title):
    return found_title.lower() in title.lower()
  
  def scrape(self, url):
    '''Returns the price of a book from Barnes & Noble query'''
    page_response = requests.get(url, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    a_tags = page_content.find_all('a')
    prices = []
    # for every book on the page
    for a_tag in a_tags:
      # if there is a title attribute
      if (a_tag.get('title')):
        # if this is the correct book
        if (self.validate_title(self.query, a_tag.get('title'))):
          children = a_tag.findChildren("span" , recursive=False)
          if (len(children) >= 1):
            price = children[1].text
            price = price[-5:]
            price = price.replace('\n', '')
            price = price.replace('$', '')
            prices.append(float(price))

    s = 0.0
    n = 0
    for i in prices:
      n += 1 
      s += i

    return s / n
