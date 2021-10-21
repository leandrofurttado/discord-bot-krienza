from imap_tools import MailBox, AND
from datetime import date, timedelta


# MailBox é a caixa de email que cria a conexão do codigo e o email.
# def newsletter():
usuario = 'aqui_coloquei_o_email@outlook.com'
senha = 'aqui_coloquei_a_senha'

meu_email = MailBox('imap-mail.outlook.com').login(usuario, senha)

# AGORA QUE JA ESTAMOS LOGANDO NO E-MAIL, VAMOS PEGAR OS EMAILS QUE QUEREMOS

'''
EU PRECISO DE E-MAILS QUE FORAM ENVIADOS ONTEM, SOMENTE! PORTANTO IMPORTEI DA BIBLIOTECA DATETIME
DATE E TIMEDELTA PARA CALCULAR O DIA DE ONTEM!
'''
# ontem = date.today() - timedelta(days=1)   ---> FORMULA PARA PEGAR O DIA DE ONTEM.
# ontem_format = ontem.strftime('%d-%m-%Y') #FORMATAÇÃO (Y MAIUSCULO PEGA OS 4 DIGITOS DA DATA) porem nao precisou.

lista_emails1 = meu_email.fetch(
    AND(from_='newsletter@filipedeschamps.com.br', date=date.today()))

with open('newsletter.txt', 'w', encoding='utf-8') as newsletter_txt:
    for email in lista_emails1:
        newsletter_txt.write(email.text)
        print('Noticias T.I atualizadas!')
