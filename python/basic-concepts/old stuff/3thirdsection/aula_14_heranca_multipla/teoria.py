#     A
#   /   \
#  B     C
#   \   /
#     D

class A:
    def falar(self):
        print('falando lorotas em A.')


class B(A):
    def falar(self):
        print('falando lorotas em B.')


class C(A):
    def falar(self):
        print('falando lorotas em C.')


class D(C, B):


"""
A classe D herda tudo de C e de B ao mesmo tempo. mas quando tem o mesmo metodo, ela pega do primeiro atributo passado em D
Ou seja, ela pega "C". caso não tenha nada lá,ele passa pro próximo "B". novamente, não tendo nada, passa a olhar em "A" já
que "C" e "B" são herdeiros de A. ======= CASO DIAMANTE ========
"""
