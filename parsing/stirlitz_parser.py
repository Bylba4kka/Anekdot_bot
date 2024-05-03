import requests
from bs4 import BeautifulSoup as b


def stirlitz_parser():
    r = requests.get("https://pikabu.ru/story/shtirlits_i_vsevsevse_10073576")

    soup = b(r.text, 'html.parser')
    # anekdots = soup.find_all('div', class_='story-block story-block_type_text')
    anekdots = soup.find_all('li')
    list_of_anekdots = [i.text for i in anekdots if '\n' not in i]

    return list_of_anekdots
