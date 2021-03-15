import json

with open('ArquivosDeDados\herois.json', 'r', encoding='utf8') as json_personagens:
    base_herois = json.load(json_personagens)

with open('ArquivosDeDados\equipamentos.json', 'r', encoding='utf8') as json_equipamentos:
    base_equipamentos = json.load(json_equipamentos)

class Personagem():

    def __init__(self, heroi):
        self.dados_do_heroi = base_herois[heroi]
        self.slots = [base_equipamentos['equipamento1']]
        self.ferimentos = 0
        self.status = 'Vivo'

    def aplicaDano(self, dano):
        self.ferimentos += dano
        if self.ferimentos >= self.dados_do_heroi['pontos_de_vida']:
            self.status = 'Morto'

    def organizaEquipamento(self, equipamento):
        pass