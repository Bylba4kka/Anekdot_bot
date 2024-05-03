import requests
from bs4 import BeautifulSoup as b

def jew_parser():
    r = requests.get("https://4tob.ru/anekdots/tag/evrei")

    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    # anekdots = soup.find_all('p')
    list_of_anekdots = [i.text for i in anekdots]
    return list_of_anekdots