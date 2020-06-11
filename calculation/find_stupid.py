import sys

sys.path.insert(1, '/find-stupids-vk/parser_directory/')

from parser_directory import parser
from parser_directory import second_parser

black_list = ['FACE', 'Sex', 'MORGENSTERN', '18+']


def get_information(url):
    print(f'INFORMATION ABOUT PAGE: {url}')
    return parser.parsing(url)


def stupid_detector_1(url):
    print('STUPID DETECTOR 1:')
    for item in black_list:
        for i in item.split(','):
            if i in second_parser.first_parse(url):
                print('He is stupid! ' + 'Because we found this words on the page: ' + i)
            else:
                pass


def stupid_detector_2(url) -> None:
    print('STUPID DETECTOR 2:')
    for item in black_list:
        for i in item.split(','):
            if i in second_parser.second_parse(url):
                print('He is stupid! ' + 'Because we found this words on the page: ' + i)
            else:
                pass

# print(get_information('https://vk.com/dizinnes'))
# stupid_detector_1('https://vk.com/dizinnes')
# stupid_detector_2('https://vk.com/dizinnes')
