from BaseDeMonstros import Monstros
from FichaJogador import FichaJogador
from Tabuleiro import Tabuleiro

jogador1 = FichaJogador('Diego', 'heroi1', 'heroi2','heroi3')

monstro1 = Monstros('monstro3')

Tabuleiro.batalhaHeroisVsMonstros(jogador1.heroi1, monstro1)
Tabuleiro.batalhaMonstrosVsHerois(jogador1.heroi1, monstro1)
