# 📚 Textbook Price Web Scraper
> A Web Scraping API for BarterOut Future Projects

### Motivation

> Since Barnes & Noble along with many other textbook sellers don't have APIs, we needed to create web scraping tools to do this work for us.

### 🔨 Tools Used
- Python 3.6.4
- BeautifulSoup4
- Requests

### 🔥 To Run the Project
Make sure to:
1. `pip3 install requests`
2. `pip3 install beautifulsoup4`

then run `python main.py -q your_query`

## 📓 Documentation
Currently, if you run `python main.py -q your_query`, it will return the average book price for the search results that contain the title you requested from Barnes & Noble on one page.
We are using the `websites.json` file as a list of currently supported websites. This can be easily appended and maintained, and may in future versions be accessible upon request of the client. 

_*Note: These results may be inaccurate, or, the program may just crash. It is still in the very early stages of dev._

### Example Query:
`python main.py -q Calculus for Dummies`

>_Avg. price for 'Calculus for Dummies' on Barnes & Noble: $ 19.99_

### 🙌 Future Plans:
- Specify site
- Specify Query
- Specify function (what reseults it returns)
- Specify data return format (JSON, etc.)
- Anything you can dream of...
