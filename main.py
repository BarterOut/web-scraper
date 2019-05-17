import sys
import json
from scrape import BasicScraper

# list of urls from the JSON file
urls = []

# gets the website list from the JSON file
def get_websites():
  with open('websites.json') as websites_list:  
    data = json.load(websites_list)
    for p in data['websites']:
      urls.append(p)

get_websites()

# runs the scraper and gives output for some query
def run(query):
  scraper = BasicScraper(query)
  for url in urls:
    print('Avg. price for \'' + query.replace('+', ' ') + '\' on Barnes & Noble: $', scraper.scrape(url+query))

# some validation before parsing users input
if len(sys.argv) > 1:
  if sys.argv[1] == '-q':
    i = 2
    query_string = ''
    while (i < len(sys.argv)):
      query_string += (sys.argv[i] + ' ')
      i += 1
    # format the query for the url encoded request
    query_string = query_string.replace(' ', '+')
    query_string = query_string[:-1]
    run(query=query_string)
else:
  print('You need to enter a query string!')
