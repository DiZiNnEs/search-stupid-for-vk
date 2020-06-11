import sys

sys.path.insert(1, '/find-stupids-vk/parser_directory/')

from parser_directory import parser
from parser_directory import second_parser


def get_information(url):
    print(f'INFORMATION ABOUT PAGE: {url}')
    return parser.parsing(url)


def stupid_detector_1(url):
    with open('black_list', 'r+') as f:
        a = f.read()
    print('STUPID DETECTOR 1:')
    for item in a.split(','):
        for i in item.split(','):
            if i in second_parser.first_parse(url):
                print('He is stupid! ' + 'Because we found this words on the page: ' + i)
            else:
                pass


def stupid_detector_2(url) -> None:
    with open('black_list', 'r+') as f:
        a = f.read()
    print('STUPID DETECTOR 2:')
    for item in a.split(','):
        for i in item.split(','):
            if i in second_parser.second_parse(url):
                print('He is stupid! ' + 'Because we found this words on the page: ' + i)
            else:
                pass


print(get_information('https://vk.com/dizinnes'))
stupid_detector_1('https://vk.com/dizinnes')
stupid_detector_2('https://vk.com/dizinnes')
