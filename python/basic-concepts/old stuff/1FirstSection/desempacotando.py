"""
desempacotamento de listas em python
"""

lista = ['luiz','rebeca','Maria',1,2,3,5,4,5,6,7,1000]
# n1, n2 = lista
#para desempacotar uma lista é necessario atribuir todos os valores, OU SEJA o código acima está errado.
#EXISTE uma forma de você desempacotar colocando somente os valores importantes e atribuindo ao resto uma única variável
n1,n2,n3,*outra_lista,ultimo_lista = lista
  #observe que o * cria um resto e quando acrescento uma ultima variavel, ele pega o ultimo valor
print(ultimo_lista)  #resp 1000

#outro exemplo
lista_2 = ['luiz','rebeca','Maria',1,2,3,5,4,5,6,7,1000]
*outra_lista,n1,n2,n3 = lista_2
#nesse caso, o n1 será 6 / n2 será 7 / n3 será 1000
print(n1,n2,n3)

