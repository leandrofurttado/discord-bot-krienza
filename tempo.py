import requests
from bs4 import BeautifulSoup


#=========================BH=====================================
def tempo_belohorizonte():
    tempo_bh = requests.get("https://www.tempo.com/belo-horizonte.htm")
    sopa_bh = BeautifulSoup(tempo_bh.text, 'html.parser')

    temperatura_bh = sopa_bh.findAll("span", {"class": "temperatura"})
    clima_bh = sopa_bh.findAll("span", {"class": "descripcion"})

    return f"**Temperatura/Sensação em BH:** {temperatura_bh[0].text}\n\n"\
           f"**Previsão para o dia:**  {clima_bh[0].text}"
#=========================BH====================================



#========================ORIENTE==================================
def tempo_orientee():
    tempo_oriente = requests.get("https://www.tempo.com/oriente_sao-paulo-l115160.htm")
    sopa_oriente = BeautifulSoup(tempo_oriente.text, 'html.parser')

    temperatura_oriente = sopa_oriente.findAll("span", {"class": "temperatura"})
    clima_oriente = sopa_oriente.findAll("span", {"class": "descripcion"})

    return f"**Temperatura/Sensação em ORIENTE:** {temperatura_oriente[0].text}\n\n" \
           f"**Previsão para o dia:**  {clima_oriente[0].text}"
#========================ORIENTE==================================



#=======================PELOTAS===================================
def tempo_pelotass():
    tempo_pelotas = requests.get("https://www.tempo.com/pelotas.htm")
    sopa_pelotas = BeautifulSoup(tempo_pelotas.text, 'html.parser')

    temperatura_pelotas = sopa_pelotas.findAll("span", {"class": "temperatura"})
    clima_pelotas = sopa_pelotas.findAll("span", {"class": "descripcion"})

    return f"**Temperatura/Sensação em PELOTAS:** {temperatura_pelotas[0].text}\n\n" \
           f"**Previsão para o dia:**  {clima_pelotas[0].text}"
#=======================PELOTAS===================================



#=======================RIO DE JANEIRO===================================
def tempo_rio():
    tempo_rj = requests.get("https://www.tempo.com/rio-de-janeiro_rio-de-janeiro-l12987.htm")
    sopa_rj = BeautifulSoup(tempo_rj.text, 'html.parser')

    temperatura_rj = sopa_rj.findAll("span", {"class": "temperatura"})
    clima_rj = sopa_rj.findAll("span", {"class": "descripcion"})

    return f"**Temperatura/Sensação em RIO DE JANEIRO:** {temperatura_rj[0].text}\n\n" \
           f"**Previsão para o dia:**  {clima_rj[0].text}"

#=======================RIO DE JANEIRO===================================



#======================= PALMAS ===================================
def tempo_palmass():
    tempo_palmas = requests.get("https://www.tempo.com/palmas_tocantins-l110074.htm")
    sopa_palmas = BeautifulSoup(tempo_palmas.text, 'html.parser')

    temperatura_palmas = sopa_palmas.findAll("span", {"class": "temperatura"})
    clima_palmas = sopa_palmas.findAll("span", {"class": "descripcion"})

    return f"**Temperatura/Sensação em PALMAS:** {temperatura_palmas[0].text}\n\n" \
               f"**Previsão para o dia:**  {clima_palmas[0].text}"
#======================= PALMAS ===================================
