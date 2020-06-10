import requests
import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs

#url = input('Enter a VK user: ')
url = 'https://vk.com/azelyaalibekova'


def selenium_browser() -> webdriver:
    browser = webdriver.Chrome()
    browser.get(url)
    #element = browser.find_element_by_css_selector('.noselect')
    element = browser.find_element_by_id('profile_groups_link')
    browser.execute_script('arguments[0].click();', element)
    return browser


def parsing() -> None:
    html = selenium_browser().page_source
    soup = bs(html, 'html.parser directory')
    title = soup.select_one('title').text
    profile_info = soup.select_one('.clear_fix.profile_info_row ').text
    more_profile_info = soup.find(id='profile_all_groups')
    print(more_profile_info)
    print(profile_info)


if __name__ == '__main__':
    parsing()
