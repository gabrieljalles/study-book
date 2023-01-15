#também recebe um decorador
#não precisa nem da instância nem da classe
# somente por questão de organização, essa metodo estatico ficaria dentro da class. mas ele é independente
# um bom indicativo para o uso de staticmethod é se eu não uso nenhuma vez o self na class
# (VEJA NA AULA 14 - class logmixin )
from random import randint

class Pessoa:
    def __init__(self,nome):
        self.nome = nome
    @staticmethod # ele pode ser chamado tanto pela classe como pela instância
    def gera_id():
        rand = randint(1000,1999)
        return rand

p1= Pessoa('Gabriel')
print(Pessoa.gera_id())
