class BaseDePersonagem:
    def __init__(self, personagem):
        self.nome = personagem["nome"]
        self.ataque = personagem["ataque"]
        self.defesa = personagem["defesa"]
        self.pontos_de_vida = personagem["pontos_de_vida"]
        self.habilidade = personagem["habilidade"]

    def papa_cu(self):
        print('tome no cu')

