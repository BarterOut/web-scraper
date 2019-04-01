from bs4 import BeautifulSoup
import requests

class BasicScraper:
  def scrape(url):
    return 'scraping'

  def demo(url):
    """Return the average price of CAET from Barnes and Noble 1 page search"""
    page_response = requests.get(url, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    titles = page_content.find_all('a')
    prices = []
    for i in titles:
      if (i.get('title')):
        children = i.findChildren("span" , recursive=False)
        if (len(children) >= 1):
          price = children[1].text
          price = price[2:]
          price = price.strip('\n')
          prices.append(float(price))

    s = 0.0
    n = 0
    for i in prices:
      n += 1 
      s += i

    return s / n