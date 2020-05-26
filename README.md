# 📚 Textbook Price Web Scraper
> A Web Scraping API for BarterOut Future Projects

### 📊 Motivation

> Since Barnes & Noble along with many other textbook sellers don't have APIs, we needed to create web scraping tools to do this work for us.

### 🔨 Tools Used
- Python 3.6.4
- BeautifulSoup4
- Requests
- Flask
- JSON

### 🔥 To Run the Project
Make sure to have Docker and docker-compose installed.

Then run `docker-compose up` or with the `-d` flag.

## 📓 Documentation
Currently, if you run `docker-compose up`, it will spin up a local dev server API that
you can send requests to.

_*Note: These results may be inaccurate, or, the program may just crash. It is still in the very early stages of dev._

### Example Query:
```json
{
  "price": "89.9513043478261"
}
```

>_Avg. price for 'Mind on Statistics' on Google: $ 105.79_

### 🙌 Future Plans:
- Specify site
- Specify Query
- Specify function (what reseults it returns)
- Specify data return format (JSON, etc.)
- Anything you can dream of...
