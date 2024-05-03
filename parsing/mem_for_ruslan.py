import requests
from bs4 import BeautifulSoup as b


def mem_for_ruslan_parser():
    r = requests.get("https://pikabu.ru/story/shutki_pro_tvoyu_zhirnuyu_mamu_1834442")

    soup = b(r.text, 'html.parser')

    text_div = soup.find('div', class_='story-block_type_text')

    jokes_list = [joke.strip() for joke in text_div.stripped_strings]

    return jokes_list
