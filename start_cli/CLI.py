import sys

sys.path.insert(1, '/find-stupids-vk/calculation/')

from calculation import find_stupid

URL = input('Link to VK page: ')

find_stupid.get_information(URL)
find_stupid.stupid_detector_1(URL)
find_stupid.stupid_detector_2(URL)
