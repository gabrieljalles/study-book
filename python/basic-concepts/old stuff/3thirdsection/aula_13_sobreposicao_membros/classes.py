# sobreposicao de metodos
# veja que o falar está em pessoa e em cliente VIP, o falar do vip sobrepos o de pessoa

class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__


    def falar(self):
        print(f'{self.nomeclasse} está falando')

class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} comprando...')

    def falar(self):
        print(f'{self.nomeclasse} está falando...')

class ClienteVIP(Cliente): #TUDO QUE TEM em cliente tem em clientevip, e tudo que tem em pessoa tem em clienteVIP
    def __init__(self,nome,idade,sobrenome):
        Pessoa.__Init__(self,nome,idade)# estou chamando o construtor da super Pessoa
        self.sobrenome = sobrenome # estou criando especificamente SOBRENOME em cliente vip


    def falar(self):
        super().falar() # nesse caso, não é bem uma sobreposicao. estou dizendo para executar primeiro da classe super
        Pessoa.falar(self) # estou chamando a classe pessoa, é necessario, nesse caso, passar self ou o atributo desejado
        Cliente.falar(self)# estou chamando a classe Cliente....
        print(f'{self.nome}{self.sobrenome}')

#observe as bolinhas azuis, elas dizem quem esta sobrepondo quem