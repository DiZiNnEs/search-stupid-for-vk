import requests
from bs4 import BeautifulSoup as bs

black_list = ['color']

def first_parse(url):
    request_to_page = requests.get(url)
    html = bs(request_to_page.content, 'html.parser')
    return html.text


def second_parse(url):
    request_to_page = requests.get(url)
    html = bs(request_to_page.content, 'html.parser')
    return list(html.find_all())


print(second_parse('https://vk.com/korol_rarka'))
for item in black_list:
    if item in second_parse('https://vk.com/korol_rarka'):
        print('He is dolboeb')
    else:
        print('He is good boy or girl')