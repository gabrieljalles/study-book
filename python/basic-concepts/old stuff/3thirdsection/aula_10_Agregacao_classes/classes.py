# AGREGAÇÃO  está situada dentro da associação, uma classe usa outra classe como parte de sí
# o carro existe sem as rodas, as rodas existem sem o carro,  mas o carro não funciona adequadamente sem as rodas


# observe que carrinho de compras existe sem o produto, mas tudo que ela vai fazer, precisa de um produto
class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def excluir(self,produto):
        self.produtos.pop(produto)

    def inserir(self, produto):
        self.produtos.append(produto)

    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return f'O total da sua compra é de R$ {total}'


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor



