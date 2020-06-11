import requests
from bs4 import BeautifulSoup as bs

black_list = ['Kuat', 'Electron', '6']


def first_parse(url) -> str:
    request_to_page = requests.get(url)
    html = bs(request_to_page.content, 'html.parser')
    return html.text


def second_parse(url) -> str:
    request_to_page = requests.get(url)
    html = bs(request_to_page.content, 'html.parser')
    return str(html.find_all())


def stupid_find() -> None:
    with open('black_list', 'r+') as f:
        a = f.read()
    for item in a.split(','):
        for i in item.split(','):
            if i in second_parse('https://vk.com/dizinnes'):
                print('He is stupid! ' + 'Because we found this words on the page: ' + i)
            else:
                print('He is good human')


print(stupid_find())
