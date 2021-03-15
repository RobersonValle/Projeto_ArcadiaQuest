from BaseDePersonagem import Personagem

class FichaJogador:
    def __init__(self, nome, heroi1, heroi2, heroi3):
        self.nome = nome
        self.heroi1 = Personagem(heroi1)
        self.heroi2 = Personagem(heroi2)
        self.heroi3 = Personagem(heroi3)
        self.moedas = 0

    def __str__(self):
        return f'{self.heroi1}'
        # return f"{self.nome}, {self.heroi1['nome']}, {self.heroi2}, {self.heroi3}, {self.moedas}"