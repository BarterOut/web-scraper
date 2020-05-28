from flask import Flask, jsonify, request
from lib.scrape import Scraper

# create the Flask app
app = Flask(__name__)

# list of urls to search from
urls = [
  'https://www.google.com/search?q='
]

@app.route('/api/query/', methods=['GET'])
def get_price():
  title = request.args.get('title')
  scraper = Scraper(urls)
  price = scraper.scrape(title)
  return { 'price': price }, 200

def run():
  app.run(debug=True, host='0.0.0.0', port=3000)