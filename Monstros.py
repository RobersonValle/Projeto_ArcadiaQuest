class BaseDeMonstros:
    def __init__(self, monstro):
        self.nome = monstro["nome"]
        self.ataque = monstro["ataque"]
        self.defesa = monstro["defesa"]
        self.pontos_de_vida = monstro["pontos_de_vida"]
        self.hit_kill = monstro["hit_kill"]

