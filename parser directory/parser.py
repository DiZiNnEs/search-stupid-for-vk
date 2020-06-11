import requests
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs

# url = input('Enter a VK user: ')
url = 'https://vk.com/tamikmanyeah32'


def selenium_browser() -> webdriver:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(url)
    try:
        element = browser.find_element_by_css_selector('.header_label.fl_l')
        browser.execute_script('arguments[0].click();', element)
    except Exception as element:
        print(f'Users {url} is private VK page')
    return browser


def parsing() -> str:
    html = selenium_browser().page_source
    soup = bs(html, 'html.parser')
    try:
        title = soup.select_one('title').text
        print('Title: ' + title)

        profile_short_info = soup.select_one('.profile_info.profile_info_short').text
        print('Short a info: ' + profile_short_info)

        profile_full_info = soup.select_one('.profile_info.profile_info_full').text
        print('Full info' + profile_full_info)

        counts_module = soup.select_one('.counts_module').text
        print('All friends followers and etc: ' + counts_module)

        following = soup.select_one('span.header_count.fl_l').text
        print('Following: ' + following)

        group_name = soup.select_one('.module_body.clear_fix').text
        print('Group name: ' + group_name)

        posts_on_wall = soup.select_one('.wall_text').text
        print(posts_on_wall)

        status = soup.select_one('.current_text').text
        print('Status:' + status)

        result = (f'''
Title: {title},
Status: {status},
Short info: {profile_short_info},
Full info: {profile_full_info},
Additional information: {counts_module},
Following: {following},
Short groups name: {group_name},
Post on the wall: {posts_on_wall}
        ''')
        return result
    except:
        pass


if __name__ == '__main__':
    print(parsing())
