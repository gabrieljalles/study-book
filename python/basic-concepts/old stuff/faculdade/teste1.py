class PrimeiraClasse:
    def __Init__(self,nome):
        self.nome = nome

    def imprimir_mensagem(self,nome):
        print(f'ola {nome},seja bem vindo ao mundo')

objeto = PrimeiraClasse()
objeto.imprimir_mensagem('gabriel')

imprimir_mensagem('gabriel')