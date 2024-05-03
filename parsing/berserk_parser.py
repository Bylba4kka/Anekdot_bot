import os

import requests
from bs4 import BeautifulSoup as b


def berserk_parser():
    urls = ['https://pikabu.ru/tag/%D0%91%D0%B5%D1%80%D1%81%D0%B5%D1%80%D0%BA%2C%D0%9C%D0%B5%D0%BC%D1%8B',
            'https://pikabu.ru/tag/%D0%91%D0%B5%D1%80%D1%81%D0%B5%D1%80%D0%BA%2C%D0%9C%D0%B5%D0%BC%D1%8B?page=2',
            'https://pikabu.ru/tag/%D0%91%D0%B5%D1%80%D1%81%D0%B5%D1%80%D0%BA%2C%D0%9C%D0%B5%D0%BC%D1%8B?page=3']
    berserk_list = list()
    for url in urls:
        r = requests.get(url)

        soup = b(r.text, 'html.parser')

        img_tags = soup.find_all('img', class_='story-image__image')

        for i in img_tags:
            img_url = i['data-large-image']
            berserk_list.append(img_url)

    return berserk_list
