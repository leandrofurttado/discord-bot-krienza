
from random import randint, uniform

class Acontecimentos():
    def setFomeAndSaude(self):
        sorteio = randint(3, 7)
        self.fome += sorteio
        sorteio2 = sorteio - 2
        self.saude -= sorteio2
        if self.fome > 95:
            self.saude -= 60

    def setSaldo(self):
        sorteio = uniform(20, 50)
        self.saldo_original += sorteio

    def envelhecer(self):
        self.idade += 1
        self.saude += 50

