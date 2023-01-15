# A relação de associação se da pela realação de duas classes mas nenhuma classe está  dependente da outra;
# a exclusão de uma não muda a outra

from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('gabriel')
caneta = Caneta ('BIC')


print(escritor.nome)
print(caneta.marca)
caneta.escrever()

escritor.ferramenta = MaquinaDeEscrever()  # estou associando o atributo vazio do escritor (ferramenta) a classe maquina de escrever
escritor.ferramenta.escrever() # ao associar, estou dando todas as propriedades disponíveis da maquina para a ferramenta do escritor
#nesse caso, estou dando até o metodo ESCREVER da maquina.


"""
Conclusão:
    Associacao, se eu apagar qualquer classe, a outra não deixa de existir.
"""