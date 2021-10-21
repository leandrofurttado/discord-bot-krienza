import requests
from bs4 import BeautifulSoup

def jogos_libertadores():
    site_libertadores = requests.get("https://www.placardefutebol.com.br/copa-libertadores")
    sopa_da_libertadores = BeautifulSoup(site_libertadores.text, 'html.parser')
    search_libertadores = sopa_da_libertadores.findAll("div", {"class": "container content"})

    jogos_libertadores = search_libertadores[0].text.replace('\n', ' ').replace('          ', '\n').replace('     ', '')

    return jogos_libertadores


def grupos_libertadores():
    site_libertadores = requests.get("https://www.placardefutebol.com.br/copa-libertadores")
    sopa_da_libertadores = BeautifulSoup(site_libertadores.text, 'html.parser')
    search_libertadores = sopa_da_libertadores.findAll("div", {"class": "container content"})

    fase_de_grupos = (search_libertadores[1].text.replace('\n', ' ').replace('  ', '\n').replace('   ', '\n').replace(
        ' Fase de Grupos',
        '').replace('Equipe Pontos J V E D SG', 'Ordem: Time - Pts - J - V - E- D - SG'))

    return fase_de_grupos
