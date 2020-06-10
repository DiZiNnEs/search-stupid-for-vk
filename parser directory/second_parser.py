import requests
from bs4 import BeautifulSoup as bs


def first_parse(url):
    request_to_page = requests.get(url)
    html = bs(request_to_page.content, 'html.parser')
    return html.text


def second_parse(url):
    request_to_page = requests.get(url)
    html = bs(request_to_page.content, 'html.parser')
    return list(html.find_all())


print(first_parse('https://vk.com/korol_rarka'))
