from datetime import datetime

class Pessoa:
    # vvvv esse é um metodo da classe
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # vvvv esse é um metodo da instância
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod # estou criando um metodo da classe
    def por_ano_nascimento(cls,nome,ano_nascimento): # não passo self, mas sim cls para me reverir a classe
    #como eu estou colocando o cls, eu terei acesso ao ano_atual, que também é um atribulto da classe
        idade = cls.ano_atual - ano_nascimento
        return cls(nome,idade)
    



p1 = Pessoa('Gabriel', 21)
p1.get_ano_nascimento()
print(Pessoa.ano_atual)
