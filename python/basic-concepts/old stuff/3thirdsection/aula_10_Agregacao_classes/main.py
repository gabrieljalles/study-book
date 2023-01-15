from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('camiseta',34.50)
p2 = Produto('camisolao',22.50)
p3 = Produto('jaqueta',89.50)

carrinho.inserir(p1)
carrinho.inserir(p2)
carrinho.inserir(p3)
print(carrinho.soma_total())

carrinho.lista_produto() # verificando meu carrinho
