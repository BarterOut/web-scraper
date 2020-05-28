# 📚 Textbook Price Web Scraper
> A Web Scraping API for BarterOut

### 📊 Motivation

We want to offer the average price of textbooks that you can find on our site. To do this, we decided to scrape
Google and other sites (in the future) to compute the average price of a textbook, and wrap it in an API.

### 🔨 Tools Used
- Python 3
- BeautifulSoup4
- Requests
- Flask

### 🔥 To Run the Project
Make sure to have Docker and docker-compose installed.

Then run `docker-compose up` or with the `-d` flag.

## 📓 Documentation
Currently, if you run `docker-compose up`, it will spin up a local dev server API that
you can send requests to.

_*Note: These results may be inaccurate, or, the program may just crash. It is still in the very early stages of dev._

### Example Query:
`GET localhost:3000/api/query/?title=Mind+on+Statistics`

---
Response:
```json
{
  "price": "89.9513043478261"
}
```

### 🙌 Future Plans:
- Specify the query site to scrape from
- Specify function (what results it returns)
- Find best (lowest) price and provide URL
- Anything you can dream of...
