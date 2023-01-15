from abc import ABC, abstractmethod

class Conta:

    def __init__(self, clienteid, saldo, agencia, banco):
        self.clienteid = clienteid
        self.saldo = saldo
        self.agencia = agencia
        self.banco = banco

    @abstractmethod
    def sacar(self, valor):
        if self.saldo >= valor:
            print(f'saldo anterior : {self.saldo}')
            print(f'saque efetuado com sucesso')
            self.saldo -= valor
            self.consultar_saldo()
        else:
            print(f'infelizmente, você não possui o valor de {valor} reais  disponível para saque.')
            self.consultar_saldo()

    def depositar(self, valor):
        self.saldo += valor

    def consultar_saldo(self):
        print(f'saldo atual: {self.saldo} ')

    def colsultar_detalhes(self):
        print(f'ID do cliente: {self.clienteid}')
        print(f'SALDO do cliente: {self.saldo}')
        print(f'AGENCIA do cliente: {self.agencia}')
        print(f'BANCO do cliente: {self.clienteid}')


class Cpoupanca(Conta):

    def __init__(self, clienteid, saldo, agencia, banco):
        super().__init__(clienteid, saldo, agencia, banco)


class Ccorrente(Conta):

    def __init__(self, clienteid, saldo, agencia, banco,limite):
        super().__init__(clienteid, saldo, agencia, banco)
        self.limite = limite

    def sacar(self,valor):
        if (self.saldo + self.limite) >= valor:
            self.consultar_saldo()
            self.saldo -= valor
            self.consultar_saldo()
        else:
            print(f'você possui {self.saldo} e o seu limite é de {self.limite}, infelizmente não podemos efetuar o saque')







f1 = Conta('gabriel', 200, 2, 222)
print(f1.clienteid)
f1.sacar(10)
f1.sacar(250)