import requests
import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs

#url = input('Enter a VK user: ')
url = 'https://vk.com/aimechkooo'


def selenium_browser() -> webdriver:
    browser = webdriver.Chrome()
    browser.get(url)
    #element = browser.find_element_by_css_selector('.noselect')
    #element = browser.find_element_by_id('profile_groups_link')
    #browser.execute_script('arguments[0].click();', element)
    return browser


def parsing() -> None:
    html = selenium_browser().page_source
    soup = bs(html, 'html.parser')
    try:

        title = soup.select_one('title').text
        print(title)

        profile_short_info = soup.select_one('.profile_info.profile_info_short').text
        print(profile_short_info)

        profile_full_info = soup.select_one('.profile_info.profile_info_full').text
        print(profile_full_info)

        status = soup.select_one('.current_text').text
        print(status)
    except:
        pass



if __name__ == '__main__':
    parsing()
