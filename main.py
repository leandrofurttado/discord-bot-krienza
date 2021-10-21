import discord
from tamagotchi import Tamagotchi
import tabelacovid
import tempo
from datetime import datetime
from locale import setlocale, LC_ALL
import FraseDoDia_script
import jogosfut
import rastreio_correios
import newsletter_filipedeschamps

client = discord.Client()

intents = discord.Intents.default()
intents.members = True
setlocale(LC_ALL, '')

with open('backup_idade.txt', 'r+') as backup:
    idade_backup = backup.readline()
    player = Tamagotchi('Krienza', int(idade_backup))
    mensagens_idade = []
    nivel_fome = []


@client.event
async def on_ready():
    print('O BOT ESTÁ FUNCIONANDO!')
    canal_send = client.get_channel(834493420080857098)
    await canal_send.send('Fui ligado! Estou online hein?!')


@client.event
async def on_message(mensagem):
    conteudo = mensagem.content.lower()
    canal = mensagem.channel
    canal_noticiasti = client.get_channel(890593204993392691)
    canal_rastreio = client.get_channel(847823229704077342)
    author = mensagem.author.name
    mencionar = mensagem.author.mention

    if author == "Krienza":  # evitar erro de loop infinito do bot interagindo com ele mesmo
        return
# ======================         COMMANDS          ==========================================
    if conteudo == "!comandos".lower():
        embed = discord.Embed(title="=====COMANDOS KRIENZA======",
                              description="!loja --> Comprar comidas\n"
                                          "!inventario --> Usar itens comprados\n"
                                          "!info --> Ver vida/fome/KrienzaPoins\n"
                                          "!tempo (nome) --> Ver temperatura das cidades dos membros\n"
                                          "!covid --> Ver vacinação e casos de covid em tempo real\n"
                                          "!libertadores --> Ver como anda a libertadores em tempo real\n", color=255255)
        await canal.send(embed=embed)

# ==========================================================================================
# =================================RASTREIO CORREIOS========================================
    if "!noticiasti" in conteudo:
        embed = discord.Embed(title="====NOTÍCIAS ATUAIS DO MUNDO DA TECNOLOGIA:====",
                              description='Eae meu chapa!\n'
                                          'Vasculhei o email do Leandro e encontrei as noticias do dia!\n'
                                          'Segue abaixo o anexo com todas as notícias do mundo da tecnologia! :D\n'
                                          '\nCréditos: Newsletter Filipe Deschamps.', color=255255)
        await canal_noticiasti.send(embed=embed)
        await canal_noticiasti.send(file=discord.File(r'.\newsletter.txt'))
        embed2 = discord.Embed(title="SE ESTIVER VAZIO É POR QUE A NOTÍCIA NÃO SAIU AINDA, AGUARDE!\n"
                               "Horário que é lançado novas notícias: 11h00",
                               description='', color=255255)
        await canal_noticiasti.send(embed=embed2)

# ==========================================================================================
# =================================RASTREIO CORREIOS========================================
    if "!correios" in conteudo:
        try:
            codigo = mensagem.content.replace('!correios', '').replace(' ', '')
            embed = discord.Embed(title="====DADOS DA SUA MERCADORIA:====",
                                  description=rastreio_correios.rastreia(str(codigo)), color=255255)

            await canal_rastreio.send(embed=embed)
        except Exception:
            await canal.send('Mercadoria não identificada!')

# ==========================================================================================

# ===================================TEMPO:=================================================
    if conteudo == "!tempo belo horizonte".lower():
        dt = datetime.now()
        formatacao = dt.strftime('%A, %d de %B de %Y')
        await canal.send("Minha nave está indo até o local para medir o clima, aguarde...")
        embed = discord.Embed(title="============TEMPO  BH=============="
                              f"\n\n{formatacao}",
                              description=tempo.tempo_belohorizonte(), color=255255)
        await canal.send(embed=embed)

    if conteudo == "!tempo oriente".lower():
        dt = datetime.now()
        formatacao = dt.strftime('%A, %d de %B de %Y')
        await canal.send("Minha nave está indo até o local para medir o clima, aguarde...")
        embed = discord.Embed(title="============TEMPO ORIENTE=============="
                                    f"\n\n{formatacao}",
                              description=tempo.tempo_orientee(), color=255255)
        await canal.send(embed=embed)

    if conteudo == "!tempo pelotas".lower():
        dt = datetime.now()
        formatacao = dt.strftime('%A, %d de %B de %Y')
        await canal.send("Minha nave está indo até o local para medir o clima, aguarde...")
        embed = discord.Embed(title="============TEMPO PELOTAS=============="
                                    f"\n\n{formatacao}",
                              description=tempo.tempo_pelotass(), color=255255)
        await canal.send(embed=embed)

    if conteudo == "!tempo rio de janeiro".lower():
        dt = datetime.now()
        formatacao = dt.strftime('%A, %d de %B de %Y')
        await canal.send("Minha nave está indo até o local para medir o clima, aguarde...")
        embed = discord.Embed(title="============TEMPO RIO DE JANEIRO=============="
                                    f"\n\n{formatacao}",
                              description=tempo.tempo_rio(), color=255255)
        await canal.send(embed=embed)

    if conteudo == "!tempo palmas".lower():
        dt = datetime.now()
        formatacao = dt.strftime('%A, %d de %B de %Y')
        await canal.send("Minha nave está indo até o local para medir o clima, aguarde...")
        embed = discord.Embed(title="============TEMPO PALMAS=============="
                                    f"\n\n{formatacao}",
                              description=tempo.tempo_palmass(), color=255255)
        await canal.send(embed=embed)

# ==========================================================================================

# ===============================COVID INFORMATION==========================================
    if conteudo == "!covid".lower():
        await canal.send("Buscando informações...")
        dt = datetime.now()
        formatacao = dt.strftime('%A, %d de %B de %Y')
        embed = discord.Embed(title="======INFORMAÇÕES SOBRE O COVID NO BRASIL======"
                                    f"\n\n{formatacao}\n\n",
                              description=tabelacovid.covid(), color=255255)
        await canal.send(embed=embed)


# ==========================================================================================

# ===============================JOGOS LIBERTADORES==========================================
    if conteudo == "!libertadores":
        await canal.send("Aguarde...")
        embed = discord.Embed(title="𝚄𝚕𝚝𝚒𝚖𝚘𝚜 𝚓𝚘𝚐𝚘𝚜 𝚍𝚊 𝚕𝚒𝚋𝚎𝚛𝚝𝚊𝚍𝚘𝚛𝚎𝚜.",
                              description=jogosfut.jogos_libertadores() + '\nPara ver os grupos digite:'
                                                                          ' !grupos libertadores', color=255255)
        await canal.send(embed=embed)

    if conteudo == "!grupos libertadores":
        await canal.send("Aguarde...")
        embed = discord.Embed(title="𝙵𝙰𝚂𝙴 𝙳𝙴 𝙶𝚁𝚄𝙿𝙾𝚂 𝙻𝙸𝙱𝙴𝚁𝚃𝙰𝙳𝙾𝚁𝙴𝚂.",
                              description=jogosfut.grupos_libertadores(), color=255255)
        await canal.send(embed=embed)


# ==========================================================================================
# ===============================FRASE DO DIA ==============================================
    if conteudo == '!frasedodia':
        embed = discord.Embed(title="A FRASE DO DIA PARA VOCÊ É:",
                              description=FraseDoDia_script.frase_do_dia(), color=255255)
        await canal.send(embed=embed)

# ==========================================================================================

    if conteudo == "!info".lower():
        if len(mensagens_idade) > 167:
            player.envelhecer()
            await canal.send(f"**Eu fiquei mais velho com tantas mensagens! Agora tenho {player.idadeAtual()} anos**")
            await canal.send("https://i.gifer.com/origin/4a/4a6d6de5bff1d841e20e08fcfc35f154_w200.gif")
            with open('backup_idade.txt', 'w+') as backup:
                backup.write(str(player.idade))
            await canal.send(embed=player.atributosGerais())
            mensagens_idade.clear()
        else:
            await canal.send(embed=player.atributosGerais())


# ========================== AUMENTO DE FOME POR MENSAGENS ================================================
    if 'a' or 'b' or 'c' or 'd' or 'e' or 'f' in conteudo:
        mensagens_idade.append('.')
        nivel_fome.append('.')
        if len(mensagens_idade) > 167:
            player.envelhecer()
            await canal.send(f"**Eu fiquei mais velho com tantas mensagens! Agora tenho {player.idadeAtual()} anos**")
            await canal.send("https://i.gifer.com/origin/4a/4a6d6de5bff1d841e20e08fcfc35f154_w200.gif")
            with open('backup_idade.txt', 'w+') as backup:
                backup.write(str(player.idade))
            mensagens_idade.clear()

        else:
            # await canal.send("Detectei!")
            pass
# ==========================================================================
# ========================== GANHO DE KRIENZA POINTS POR RISADA ================================================
# ========================== LOJA ================================================
    if conteudo == "!loja".lower():
        embed = discord.Embed(title="======LOJA DO KRIENZA======",
                              description="Digite o nome correto da comida que deseja:\n"
                              "|🍎| Maçã = 200 KP 💵\n"
                              "|🍌| Banana = 300 KP 💵\n"
                              "|🍐| Pêra = 550 KP 💵", color=255255)
        await canal.send(embed=embed)

    if conteudo == 'maçã'.lower():
        if player.saldo() < 200:
            await canal.send("Você não tem KP suficientes para comprar uma Maçã!")
        else:
            embed = discord.Embed(title="Você comprou uma Maçã para o Krienza! Digite !inventario para vê-la",
                                  color=255255)
            player.comprarAlimento("Maçã")
            await canal.send(embed=embed)
    if conteudo == 'banana'.lower():
        if player.saldo() < 300:
            await canal.send("Você não tem KP suficientes para comprar uma Banana!")
        else:
            embed = discord.Embed(title="Você comprou uma Banana para o Krienza! Digite !inventario para vê-la",
                                  color=255255)
            player.comprarAlimento("Banana")
            await canal.send(embed=embed)
    if conteudo == 'pêra'.lower():
        if player.saldo() < 550:
            await canal.send("Você não tem KP suficientes para comprar uma Pêra!")
        else:
            embed = discord.Embed(title="Você comprou uma Pêra para o Krienza! Digite !inventario para vê-la",
                                  color=255255)
            player.comprarAlimento("Pêra")
            await canal.send(embed=embed)
# ========================== LOJA ================================================
# ========================== INVENTARIO/COMER ================================================
    if conteudo == "!inventario":
        if player.comidas_player == []:
            embed = discord.Embed(title="Seu inventário está vazio, vá comprar comida para Krienza"
                                        " basta digitar !loja", color=255255)
            await canal.send(embed=embed)
        else:
            embed = discord.Embed(title="Seu inventário contém:", description=f"**{player.comidas_player}**\n\n\n"
                                  f"**Para dar ao Krienza algo do inventário digite !usar (nome do item)**",
                                  color=255255)
            await canal.send(embed=embed)

    if conteudo == "!usar maçã":
        if player.fome <= 2:
            await canal.send('Krienza já está bem alimentado! Não precisa alimenta-lo.')
            return
        if "Maçã" in player.comidas_player:
            embed = discord.Embed(
                title="Você alimentou Krienza com uma maçã :)", color=255255)
            player.fome -= 20
            await canal.send(embed=embed)
            await canal.send('https://www.imagensanimadas.com/data/media/329/maca-imagem-animada-0027.gif')
            player.comidas_player.remove("Maçã")
        else:
            embed = discord.Embed(title="Você não tem esse item no seu inventário para usar. Vá comprar.",
                                  color=255255)
            await canal.send(embed=embed)

    if conteudo == "!usar banana":
        if player.fome <= 2:
            await canal.send('Krienza já está bem alimentado! Não precisa alimenta-lo.')
            return
        if "Banana" in player.comidas_player:
            embed = discord.Embed(
                title="Você alimentou Krienza com uma Banana :)", color=255255)
            player.fome -= 30
            await canal.send(embed=embed)
            await canal.send('https://media0.giphy.com/media/1s0P1OJ1pGIYQryEGI/source.gif')
            player.comidas_player.remove("Banana")
        else:
            embed = discord.Embed(title="Você não tem esse item no seu inventário para usar. Vá comprar.",
                                  color=255255)
            await canal.send(embed=embed)

    if conteudo == "!usar pêra":
        if player.fome <= 2:
            await canal.send('Krienza já está bem alimentado! Não precisa alimenta-lo.')
            return
        if "Pêra" in player.comidas_player:
            embed = discord.Embed(title="Você alimentou Krienza com uma Pêra Mágica e ganhou +20 de SAÚDE! :)",
                                  color=255255)
            player.fome -= 60
            player.saude += 20
            await canal.send(embed=embed)
            await canal.send('https://i.pinimg.com/originals/9b/4b/c6/9b4bc644c9392206af05815b1d435b94.gif')
            player.comidas_player.remove("Pêra")
        else:
            embed = discord.Embed(title="Você não tem esse item no seu inventário para usar. Vá comprar.",
                                  color=255255)
            await canal.send(embed=embed)

# ========================== INVENTARIO/COMER ================================================

# ========================== PALAVRAS PARA RESPONDER =========================================
    if "oi krienza".lower() in conteudo:
        await canal.send("Eai, beleza?")

    if "Krienza você está bem?".lower() in conteudo:
        await canal.send('Estou bem e você?')


# =============================================================================================

    if conteudo == "!programadorleandro".lower():
        await canal.send(f"Valor do contador de idade: {len(mensagens_idade)} **essa informação é informação do codigo"
                         f"para quem chamou ela**")


@client.event
async def on_member_join(member):
    canal = client.get_channel(506943719388479491)
    await canal.send("Seja bem-vindo, " + member.mention + "!" + " não repara a bagunça.")


client.run("SEU-TOKEN-AQUI")
