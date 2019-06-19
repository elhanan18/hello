from flask import Flask, jsonify
from flask import request
from bs4 import BeautifulSoup
import requests
import re

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello():
    if request.method == 'POST':
        data = request.get_json()
        page = requests.get(data["url"])
        soup = BeautifulSoup(page.content, 'html.parser')
        links = soup.findAll('a', attrs={'href': re.compile("/wiki/")})
        links_list = []
        for link in links:
            links_list.append("https://en.wikipedia.org" + link['href'])
        res = {"linked_articles": links_list}
        res = jsonify(res), 200
        return res


if __name__ == "__main__":
    app.run()
