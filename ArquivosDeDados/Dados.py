# dados de ataque
# ataque_melee = 3
# ataque_distancia = 2
# ataque_critico = 1
#
# dados de defesa
# defesa = 1
# defesa_critico = 1

from random import randint #Biblioteca que gera numeros dinâmicos inteiros.

class RolaDados:
    def __init__(self):
        pass

    def rolaDados(self, quantidade_de_dados=1): #Função que recebe a quantidade de dados que vai rolar (Ataque e Defesa).
        resultados = []
        for i in range(0, quantidade_de_dados):
            dados = randint(1, 6) #Gera um numero aleatório de 1 à 6.
            resultados.append(dados) #Adiciona em uma lista todos os resultados.
        return resultados

    def verificaAtaque(self, valores_de_ataque): #Função que vefica o resultado de ataque.
        resultado = []
        for valor in valores_de_ataque:
            if valor == 1 or valor == 2 or valor == 3: #Verifica se foi um acerto melee
                resultado.append('m')
            elif valor == 4 or valor == 5: #Verifica se foi um acerto a distância
                resultado.append('d')
            elif valor == 6: #Verifica se foi um acerto critico
                resultado.append('c')
                ataque_extra = self.rolaDados() #Solicita mais uma rolagem de dados.
                valores_de_ataque.append(ataque_extra[0]) #Adiciona a rolagem de dados extra no final da fila para conferência.
        # print(len(valores_de_ataque))
        # print(valores_de_ataque)
        return resultado, len(valores_de_ataque)

    def verificaDefesa(self, valores_de_defesa):
        resultado = []
        for valor in valores_de_defesa:
            if valor == 1: #Verifica se foi um acerto da defesa.
                resultado.append('d')
            elif valor == 6: #Verifica se foi um acerto critico.
                resultado.append('c')
                defesa_extra = self.rolaDados() #Solicita mais uma rolagem de dados.
                valores_de_defesa.append(defesa_extra[0]) #Adiciona a rolagem de dados extra no final da fila para conferência.
        # print(len(valores_de_defesa))
        # print(valores_de_defesa)
        return resultado, len(valores_de_defesa)

    def mostraResultado(self, acao, tipo_de_ataque, dados):
        acertos = 0
        if acao == 'ataque':
            resultado, dados_rodados = self.verificaAtaque(self.rolaDados(dados))
        elif acao == 'defesa':
            resultado, dados_rodados= self.verificaDefesa(self.rolaDados(dados))

        for hit in resultado:
            if hit == tipo_de_ataque or hit == 'c':
                acertos += 1
        return acertos, dados_rodados

    def ataca(self, dados, rerolagens):
        # print('----------- Ataque -----------')
        acertos_normal, dados_normal = self.mostraResultado('ataque', 'm', dados)
        acertos_final= acertos_normal

        if rerolagens > 0 and acertos_normal < dados_normal:
            acertos_rerolagem, dados_rerodados = self.mostraResultado('ataque', 'm', rerolagens)
            acertos_final += acertos_rerolagem

        if acertos_final > dados_normal:
            acertos_final = dados_normal

        # print(f'vc rolou {dados_normal}x dados de ataque')
        # print(f'vc acertou {acertos_final}x')
        # print('----------- Ataque -----------')
        return acertos_final

    def defende(self, dados, rerolagens):
        # print('----------- Defesa -----------')
        acertos_normal, dados_normal = self.mostraResultado('defesa', 'd', dados)
        acertos_final = acertos_normal

        if rerolagens > 0 and acertos_normal < dados_normal:
            acertos_rerolagem, dados_rerodados = self.mostraResultado('defesa', 'd', rerolagens)
            acertos_final += acertos_rerolagem

        if acertos_final > dados_normal:
            acertos_final = dados_normal

        # print(f'vc rolou {dados_normal}x dados de ataque')
        # print(f'vc acertou {acertos_final}x')
        # print('----------- Defesa -----------')
        return acertos_final
