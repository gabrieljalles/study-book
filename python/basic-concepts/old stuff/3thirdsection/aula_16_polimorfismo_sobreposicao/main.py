"""
Polimorfismo é o principio que permite classes derivadas de uma mesma superclasse tenham métodos iguais, comportamentos diferentes.

"""
from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def fala(self,msg):
        pass

class B(A):
    def fala(self,msg):
        print(f'B ESTÁ FALANDO {msg}')

class C(A):
    def fala(self,msg):
        print(f'C ESTÁ FALANDO {msg}')
