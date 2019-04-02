import sys
from scrape import BasicScraper

URL = 'https://www.barnesandnoble.com/s/'

def run(query):
  print('Avg. price for ' + query + ' : $', BasicScraper.demo(URL+query))

if len(sys.argv) == 3:
  if sys.argv[1] == '-q':
    run(query=sys.argv[2])
else:
  run(query='calculus+for+dummies')
