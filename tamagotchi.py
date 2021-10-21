
import discord
from timeline import Acontecimentos

class Tamagotchi(Acontecimentos):
    comidas_player = []
    alimentos_loja = {'Maçã': 200, 'Banana': 300, 'Pêra': 550}  #ALIMENTO  /   PREÇO EM TAMA POINTS

    def __init__(self, nome, idade, fome=0, saude=100, humor=0, saldo_original=800):
        self.nome = nome
        self.idade = int(idade)
        self.fome = fome
        self.saude = saude
        self.humor = humor
        self.saldo_original = saldo_original

    def atributosGerais(self):
        if self.saude > 100:
            self.saude = 100
        if self.fome < 0:
            self.fome = 0
        if self.saude < 0:
            self.saude = 0
        if self.fome > 100:
            self.fome = 100
        mensagem = discord.Embed(title="👽 MINHAS INFOS: 👽", description=f'🎫 Meu nome: **{self.nome}**\n' \
               f'🌟 Idade: **{self.idade} anos**\n' \
               f'😋 Fome: **{self.fome}%**\n'\
               f'🩸 Saúde/Vida: **{self.saude}%**\n'\
               #f'**NIVEL DE HUMOR: {self.humor}\n'\
               f'💸 KrienzaPoints: **{self.saldo_original:.2f} KrienzaPoints**', color=255)

        return mensagem

    def idadeAtual(self):
        return self.idade

    def fome(self):
        return int(self.fome)

    def saldo(self):
        return self.saldo_original


    def comprarAlimento(self, alimento):
        if alimento in Tamagotchi.alimentos_loja:
            Tamagotchi.comidas_player.append(alimento)
            self.saldo_original -= Tamagotchi.alimentos_loja[alimento]
            print(f'Você comprou {alimento}! E ficou com o saldo de: {self.saldo_original:.2f} TamaPoints')
        else:
            print('Item não encontrado digite corretamente!')