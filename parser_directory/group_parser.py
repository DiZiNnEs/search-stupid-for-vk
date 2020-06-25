from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
import time


def selenium_browser(url) -> webdriver:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(url)
    try:
        element = browser.find_element_by_xpath('//span[contains(text(), "Following")]').click()
        time.sleep(5)
    except Exception as element:
        print(f'Users {url} is private VK page')
    return browser


def group_parsing(url):
    html = selenium_browser(url).page_source
    soup = bs(html, 'html.parser')
    try:
        groups = soup.select_one('.fans_rows.fans_idols').text
        return groups
    except:
        pass

# print(group_parsing('https://vk.com/dizinnes'))
