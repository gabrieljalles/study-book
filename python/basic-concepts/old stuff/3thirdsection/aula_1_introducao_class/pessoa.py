from datetime import datetime

class Pessoa:
    # variaveis da classe, fica constante para todos os usuários da classe
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):

        if self.falando:
            print(f'{self.nome} não consegue comer e falar ao mesmo tempo')
            return
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return

        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True

    def parar_comer(self):
        if self.falando:
            print(f'{self.nome} não está comendo, ele está falando')
            return

        if self.comendo:
            print(f'{self.nome} parou de comer')
            self.comendo = False
            return

        print(f'{self.nome} não está comendo nada')

    def falar(self, fala):
        if self.falando:
            print(f'{self.nome} não consigo falar duas coisas ao mesmo tempo')
            return

        if self.comendo:
            print(f'{self.nome} não pode falar comendo algo')
            return

        print(f'{self.nome} está falando {fala}')
        self.falando = True

    # ==================================================================================
    ##vou criar uma variável, mas dessa forma, só será válida no  metodo ini
    # variavel = 'valor'
    ##se eu criar outro metodo,a variável não estará disponível
    # def outro_metodo():
    # print(variavel) # erro
    # ==================================================================================
