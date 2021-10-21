import requests
from bs4 import BeautifulSoup


def covid():
    pagevacine = requests.get(
        "https://news.google.com/covid19/map?hl=pt-BR&mid=%2Fm%2F015fr&state=7&gl=BR&ceid=BR%3Apt-419")

    soupvacine = BeautifulSoup(pagevacine.text, 'html.parser')

    procura = soupvacine.findAll("div", {"class": "UvMayb"})
    aumento = soupvacine.findAll("div", {"class": "tIUMlb"})

    casoscovid = procura[0].text
    mortescovid = procura[1].text
    dosesaplicadas = procura[2].text
    pessoastotalvacinadas = procura[3].text

    aumento1 = aumento[0].text
    aumento2 = aumento[1].text
    porcentagem_vacinados = aumento[3].text

    pagina_request = requests.get(
        "https://github.com/wcota/covid19br/blob/master/cases-brazil-total.csv")
    sopa = BeautifulSoup(pagina_request.text, 'html.parser')

    procura = sopa.findAll("tr", {"class": "js-file-line"})

    with open("covid19dados.txt", 'w') as arquivo:
        dados_limpos = procura[1].text.replace(" ", "")
        arquivo.write(dados_limpos)

    with open("covid19dados.txt", 'r') as arquivo2:
        lista = arquivo2.readlines()
        calculo = int(lista[19]) * 100 / 212000000
        return f"**CASOS:** {casoscovid}({aumento1})\n\n" \
            f"**MORTES:** {mortescovid} ({aumento2})\n\n" \
            f"**TOTAL DE DOSES APLICADAS:** {dosesaplicadas}\n\n" \
            f"**PESSOAS TOTALMENTE VACINADAS:** {pessoastotalvacinadas}" \
            f" ({porcentagem_vacinados})\n" \
            f"**Fonte: Google**\n\n\n" \
            f"**PESSOAS TOTALMENTE VACINADAS(GitHub Leandro):** {int(lista[19])}\n" \
            f"**Porcentagem:** {calculo:.2f}%\n" \
            f"**Fonte: GITHUB Leandro**"
