"""
O MODULO DATACLASSES fornece um decorador e funções para criar automaticamente métodos, como __init__, __repr__(), __eq__
em classes definidas pelo usuário.
https://docs.python.org/pt-br/3/library/dataclasses.html
"""
from dataclasses import dataclass


# usado para facilitar o seu trabalho, não recomendado com pouco tempo de uso da linguagem.
# pode criar vícios de entendimento


@dataclass(order=True)  # veja lá em baixo o order funcionando vvvvv
class Pessoa:
    nome: str
    sobrenome: str

    #  ^^^^ pronto, a classe já está criada

    # caso ainda precise de um init existe o post init
    # um metodo que é executado logo depois do init

    def __post_init__(self):
        if not isinstance(self.nome,str):
            raise TypeError(
                f' Invalid type {type(self.nome).__name__} != str em {self}'
            )
        self.nome_completo1 = f'{self.nome} {self.sobrenome}'

    # veja a sutil diferença de com PROPERTY e SEM PROPERTY

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    def numero_serie(self):
        return f'{self.nome} {self.sobrenome}'


# lembra que para fazer uma comparacao é necessário que tenha __eq__
# o próprio dataclass já deixa isso funcionando, você pode comparar de várias formas

p1 = Pessoa('gabriel', 'jalles')
p2 = Pessoa('fernando', 'mota')

print(p1 == p2)  # viu que fica bem mais fácil ?

# com property
print(p1.nome_completo)

# sem property
# print(p1.nome_completo()) # veja que fica errado, uma vez que já coloquei o property nele
print(p1.numero_serie())

print(p1.nome)

#MOSTRANDO O ORDER
p3 = Pessoa('A', '3')
p4 = Pessoa('C', '4')
p5 = Pessoa('B', '1')
p6 = Pessoa('D', '2')

pessoas = [p3, p4, p5, p6]

print(sorted(pessoas)) # sem o order não seria possível
print(sorted(pessoas, key=lambda pessoa: pessoa.sobrenome)) # estou ordenando os nomes por ordem dos sobrenomes
print(sorted(pessoas, key=lambda pessoa: pessoa.sobrenome, reverse=True)) # estou ordenando do maior pro menor
