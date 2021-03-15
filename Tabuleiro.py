from BaseDeMonstros import Monstros
from BaseDePersonagem import Personagem
from ArquivosDeDados.Dados import RolaDados
from FichaJogador import FichaJogador


class Tabuleiro():
    def __init__(self):
        pass
        # nome_campanha = ''
        # beneficia=''
        # missoes=''
        # carta_repompensa=''
        # preparacao_especial=''
        # regras_especiais=''
        # marcadores_de_exploracao=''
        # marcadores_de_entrada_de_monstro=''
        # portais_azul=''
        # portais_vermelho = ''
        # marcadores_de_missao=''
        # localizacao_dos_monstros=''
        # localizacao_dos_herois=''

    @staticmethod
    def batalhaHeroisVsMonstros(heroi=None, monstro=None):
        # print(f'Herois: {heroi.dados_do_heroi["defesa"]}')
        # print(f'Monstro: {monstro.monstro["ataque"]}')

        dados = RolaDados()
        ataque_do_heroi = dados.ataca(heroi.slots[0]['ataque'], heroi.slots[0]['tipo_ataque'], rerolagens=0)

        if ataque_do_heroi >= monstro.monstro['over_kill']:
            monstro.aplicaDano(100)
            print(f'Pontos de ataque: {ataque_do_heroi}')

        else:
            defesa_do_monstro = dados.defende(monstro.monstro['defesa'], rerolagens=0)
            print(f'Pontos de ataque: {ataque_do_heroi}')
            print(f'Pontos de defesa: {defesa_do_monstro}')
            if ataque_do_heroi <= defesa_do_monstro:
                dano = 0
            else:
                dano = ataque_do_heroi-defesa_do_monstro
            monstro.aplicaDano(dano)

    @staticmethod
    def batalhaMonstrosVsHerois(heroi, monstro):
        dados = RolaDados()
        ataque_do_monstro = dados.ataca(monstro.monstro['ataque'], monstro.monstro['tipo_ataque'], rerolagens=0)
        defesa_do_heroi = dados.defende(heroi.dados_do_heroi['defesa'], rerolagens=0)
        print(f'Pontos de ataque do monstro: {ataque_do_monstro}')
        print(f'Pontos de defesa do heroi: {defesa_do_heroi}')
        if ataque_do_monstro <= defesa_do_heroi:
            dano = 0
        else:
            dano = ataque_do_monstro-defesa_do_heroi
        heroi.aplicaDano(dano)