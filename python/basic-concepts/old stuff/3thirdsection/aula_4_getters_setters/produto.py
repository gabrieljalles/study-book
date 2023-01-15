# vamos dizer que ao acrescentar um valor que está fora do padrão "OBSERVE O ERRO"
# podemos consertar com setter and getter
# também usamos o getter para passar um atributo privado(que só pode ser usado na classe) para fora dela ( VEJA: ASSOCIACAO_CLASSES )

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,valor):
        self._nome = valor.title() # passei as primeiras letras para maiusculo



    # Getter
    @property  # decorador
    def preco(self):
        return self._preco #por convensão usa o underline para criar uma nova variavel

    #Setter
    @preco.setter
    def preco(self,valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$','')) # pedindo para substituir o simbolo por nada

        self._preco = valor




p1 = Produto('Camiseta', 50)
p1.desconto(10)
print(p1.preco)

p2 = Produto('Caneca', 'R$15')  # OBSERVE O ERRO
print(p2.preco) # dessa forma, caso alguem escreva o simbolo do dinheiro ele é retirado pelo setter