"""
as vezes eu crio uma classe generica que não quero que ela seja usada, por exemplo:
tenho um banco e é possível que esse banco aceita conta poupanca e conta corrente.
nos dois casos são CONTAS. Posso criar uma conta GENÊRICA e dela ter essas duas contas, mas não usar a CONTA em sí.

"""
from abc import ABC, abstractmethod # para poder criar classes abstratas

class A(ABC):
    @abstractmethod
    def falar (self): # POR SER ABSTRATO, não posso mais chamar esse metodo em A, apenas nos filhos
        pass

# todo metodo abstrato, deve ser criado nas demais filhas, veja em B
class B(A):
    def falar(self):
        print('falando... B....')



