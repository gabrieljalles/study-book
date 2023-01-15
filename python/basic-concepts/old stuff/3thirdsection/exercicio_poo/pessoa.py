class Pessoa:
    """ """

    def __init__(self, nome: str, idade: int, nascimento=None):
        self.nome = nome
        self.idade = idade
        self.nascimento = nascimento


class Cliente(Pessoa):
    def __init__(self):
        super().__init__(self, nome, idade)
