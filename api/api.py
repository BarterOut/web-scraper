from flask import Flask, jsonify, request
from lib.scrape import BasicScraper
import json

app = Flask(__name__)

# list of urls from the JSON file
urls = []
# gets the website list from the JSON file
def get_websites():
  with open('./lib/websites.json') as websites_list:  
    data = json.load(websites_list)
    for p in data['websites']:
      urls.append(p)

get_websites()

@app.route('/api/query/', methods=['GET'])
def get_price():
    title = request.args.get('title')
    scraper = BasicScraper(urls)
    price = scraper.scrape(title)
    return {'price': price}, 200

def run():
    app.run(debug=True, port=3000)