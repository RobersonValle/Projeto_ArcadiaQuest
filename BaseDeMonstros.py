import json

with open('ArquivosDeDados\monstros.json', 'r', encoding='utf8') as json_monstros:
    base_monstros = json.load(json_monstros)

class Monstros():

    def __init__(self, monstro):
        self.monstro = base_monstros[monstro]
        self.ferimentos = 0
        self.recompensa = None
        self.status = 'Vivo'

    def aplicaDano(self,dano):
        self.ferimentos += dano
        if self.ferimentos >= self.monstro['pontos_de_vida']:
            self.status = 'Morto'