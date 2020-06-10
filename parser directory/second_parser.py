import requests
from bs4 import BeautifulSoup as bs


def second_parse(url):
    request_to_page = requests.get(url)
    html = bs(request_to_page.content, 'html.parser')
    print(html.text)
    print(html.find_all())
