# os objetos de uma classe são também objetos de outra classe

#Observe que tanto no cliente como no aluno tem o NOME  e IDADE
# o legal seria criar uma classe mãe (PESSOA) e depois essas duas classes filhas para não ter repeticao de atributos
# a herança vem de fora pra dentro não de dentro pra fora 
class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__


    def falar(self):
        print(f'{self.nomeclasse} está falando')


class Cliente(Pessoa): # estou dizendo que cliente herda todas as características de Pessoa
            def comprar(self):
                print(f'{self.nomeclasse} está comprando...')


class Aluno(Pessoa): # estou dizendo que Aluno herda todas as características de Pessoa
            def estudar(self):
                print(f'{self.nomeclasse} está estudando..')

