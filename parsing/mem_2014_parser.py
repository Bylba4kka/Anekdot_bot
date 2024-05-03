import requests
from bs4 import BeautifulSoup as b


def mem_2014_parser():
    r = requests.get('https://vibirai.ru/articles/top_20_memov_2014_goda-1406468')

    soup = b(r.text, 'html.parser')

    img_tags = soup.find_all(('img'), alt='')

    list_of_mem = list()

    for img_tag in img_tags:
        if img_tag['src'].startswith('//vibirai.ru/image/'):
            img = "https:" + img_tag['src']
            list_of_mem.append(img)

    return list_of_mem

