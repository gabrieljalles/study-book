from abc import ABC, abstractmethod


class Conta:
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Saldo precisa numérico")
        self._saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor do depósito precisa ser numérico")

        self._saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'AGENCIA :{self._agencia}', end=' ')
        print(f'CONTA :{self._conta}', end=' ')
        print(f'SALDO :{self._saldo}\n')

    @abstractmethod  # as formas como cada tipo de conta autoriza o saque é único.dessa forma, criamos o abstract e passamoS
    def sacar(self, valor):  # pessoalmente em cada subclasse
        pass
