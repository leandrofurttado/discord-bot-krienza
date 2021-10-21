from bs4 import BeautifulSoup
import requests


def rastreia(codigo):
    code = codigo
    site = requests.get(f'https://www.linkcorreios.com.br/?id={code}')

    soup = BeautifulSoup(site.text, 'html.parser')
    status = soup.findAll("div", {"class": "card-header"})
    convert = (status[0].text).replace('Ãtimo', 'Último').replace('destinatÃ¡rio', 'destinatário.')\
        .replace('DistribuiÃ§Ã£o', 'Distribuição')
    return convert
