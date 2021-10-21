import requests
from bs4 import BeautifulSoup


def frase_do_dia():
    url_frase = 'https://www.frasesdodia.com/'
    request_da_url = requests.get(url_frase)
    sopa_da_frase = BeautifulSoup(request_da_url.text, 'html.parser')

    for frase in sopa_da_frase.select('.phraseDia'):
        return frase.text


