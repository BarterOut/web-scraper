from bs4 import BeautifulSoup
import requests
import re

class BasicScraper:
  def __init__(self, websites):
    self.websites = websites

  def validate_title(self, title, found_title):
    return found_title.lower() in title.lower()
  
  def scrape(self, title):
    '''Returns the price of a book from Google Query'''
    title = title.replace(' ', "+") + '&tbm=shop'
    
    url = self.websites[0] + title
    html_content = requests.get(url).text

    found = re.findall(r'\$\d+\.\d+', html_content)
    avg = 0

    for price in found:
      price = price.replace('$', '')
      n_price = float(price)
      avg += n_price
      
    return str(avg/len(found))