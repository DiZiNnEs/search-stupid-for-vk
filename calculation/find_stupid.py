import sys

sys.path.insert(1, '/find-stupids-vk/parser_directory/')

from parser_directory import parser
from parser_directory import second_parser

black_list = ['FACE', 'СКРИПТОНИТ', 'молодежь', 'stay with me', 'Твои родители случайно н', 'Подкаты Категории А',
              'Мои вечные 16', 'Лирика Души', 'к тебе хочу. очень', 'Душевные цитатки', 'Гифки любовь поцелуи отн',
              'Послушай..', 'Записки о Любви', 'Есенин', 'Академия Порядочных Деви', 'Randevu', 'Я тебя люблю',
              'поколение двухтысячных', 'Секреты красоты', 'Рифмы и Панчи', 'послушай заново.', 'Kosmos',
              'закрытые цитаты', 'картины памяти горят', 'рассвет твоих чувств', 'Грустный плейлист', 'МОЛОДЫЕ',
              'случайность', 'Отбросы этого поколения', 'Zzmeyaa', 'ох', 'Patron.', 'Цитаты и Книги', '▼ Ты мой космос',
              'I n d i g o', 'Душа моя', 'океан грустных строк', 'Я Тебя Люблю', 'Baldinini', 'dаmn',
              'VSCO ФИЛЬТРЫ | инстамасоч', 'ФРЕНДЗОНА', 'ЛЮБОЛЬ', '♥..Три метра над уровнем не', 'ван лав',
              'душевная кома.', 'Академия Порядочных Девиц', 'картины памяти горят', 'рассвет твоих чувств', 'секс',
              'БОЛЬ | ЛЮБОВЬ', 'Депрессивный Призрак.', 'строчки из песен', 'и интeрес к тeбе пpoпал.',
              'я не врал, что вас всех люблю,', 'Ты — цветущая роза. Такая же прекрасная и труднодоступная.',
              'я редко проявляю интерес к людям. и чем старше становлюсь, тем хуже.', 'Dr', 'V Λ C U U M', 'Эстетика',
              'E U P H O R I A', 'Foréver.', 'Ищу тебя Кокшетау', 'KZ|vines|videos', 'Пикчи для секса',
              'твоей прекрасной юности ', 'E L E G A N T', 'ПРИЗНАВАШКИ КОКШЕТА', 'Bikkembergs', 'молодость',
              'Френдзона 18+', 'Навсегда...',
              'Spokoystvie.', 'Это Сеул, детка', 'M.', 'трахать', 'сучка', 'иметь', 'рвать', 'удовлетворять',
              'вставлять', '', '',
              '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
              '', '', '', '', '', '', '', '', ]


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
