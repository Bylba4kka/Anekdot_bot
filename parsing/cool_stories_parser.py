import requests
from bs4 import BeautifulSoup as b


def cool_stories_parser():
    r = requests.get("https://lolstory.ru/random")

    soup = b(r.text, 'html.parser')
    cool_stories = soup.find_all('span',
                                 class_="story-content_text__hrFwd text_root__SaKTE text_color-black-100__EaR_O text_typography-content-m__66RlX")

    anekdots_list = [span.get_text(strip=True) for span in cool_stories]
    return anekdots_list


