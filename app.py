from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
  return render_template("index.html")
if __name__ == "__main__":
 app.run(debug=True)
import requests
from bs4 import BeautifulSoup
def scrape_news():
  url = "https://www.flipkart.com/search?q=lenovo%20laptop%20i5%2012th%20generation%20rating%204.5&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")
  headlines = []
  for headline in soup.find_all("h3", class_="headline"):
    headlines.append(headline.text)
  return headlines
@app.route("/")
def home():
 headlines = scrape_news()
 return render_template("index.html", headlines=headlines)