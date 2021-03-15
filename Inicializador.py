from ArquivosDeDados.Dados import RolaDados
import BaseDePersonagem
import BaseDeMonstros
import json



with open('ArquivosDeDados\Campeoes.json', 'r', encoding='utf8') as json_personagens:
    dados_chars = json.load(json_personagens)

with open('ArquivosDeDados\Monstros.json', 'r', encoding='utf8') as json_monstro:
    dados_monstro = json.load(json_monstro)

char = dados_chars['char01']

player1 = BaseDePersonagem.Personagem(char)
# print(player1)
# inimigo1 = BaseDeMonstros(dados_monstro['monstro01'])

# print(player1.nome)
# print(inimigo1.nome)


# # ----------------- Teste da rolagem de dados -----------------
# dados01 = RolaDados()
# print(dados01.ataca(5, 5))
# print(dados01.defende(5, 5))
# # --------------------------------------------------------------