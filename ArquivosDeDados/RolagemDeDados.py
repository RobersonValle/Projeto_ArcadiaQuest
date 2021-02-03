# dados de ataque
# ataque_melee = 3
# ataque_distancia = 2
# ataque_critico = 1
#
# dados de defesa
# defesa = 1
# defesa_critico = 1

from random import randint

def rolaDados(quantidade_de_dados=1):
    resultados = []
    for i in range(0, quantidade_de_dados):
        dados = randint(1, 6)
        resultados.append(dados)
    return resultados

def verificaAtaque(valores_de_ataque):
    resultado = []

    print(len(valores_de_ataque))
    for valor in valores_de_ataque:
        if valor == 1 or valor == 2 or valor == 3:
            resultado.append('m')
        elif valor == 4 or valor == 5:
            resultado.append('d')
        elif valor == 6:
            resultado.append('c')
            if len(valores_de_ataque) < 8:
                ataque_extra = rolaDados(1)
                valores_de_ataque.append(ataque_extra[0])
    print(valores_de_ataque)
    return resultado

def verificaDefesa(valores_de_defesa):
    resultado = []
    print(len(valores_de_defesa))
    for valor in valores_de_defesa:
        if valor == 1:
            resultado.append('d')
        elif valor == 6:
            resultado.append('c')
            if len(valores_de_defesa) < 6:
                ataque_extra = rolaDados()
                valores_de_defesa.append(ataque_extra[0])
    print(valores_de_defesa)
    return resultado

def mostraResultado(acao, tipo_de_ataque):
    acertos = 0
    if acao == 'a':
        resultado = verificaAtaque(rolaDados(8))
    elif acao == 'd':
        resultado = verificaDefesa(rolaDados(6))

    for hit in resultado:
        if hit == tipo_de_ataque or hit == 'c':
            acertos += 1
    print (f'Você acertou {acertos}x')
    print(resultado)

def rerolagemDosDados():
    pass

mostraResultado('a', 'm')
print()
mostraResultado('d', 'd')
print()