#observe o exemplo a seguir :
d5 = { 1:'a', 2:'b', 3:'c'}
# v= d5  nesse caso não estou criando um outro dicionário, apenas estou renomeando. QUALQUER MODIFICACAO, altera os dois
# quando você usa o igual, você não está criando outro dicionário
# v[2] = "luiz"
#print(v)  #{1: 'a', 2: 'luiz', 3: 'c'}
#print(d5) #{1: 'a', 2: 'luiz', 3: 'c'}
 #observe que os dois são modificados

#agora, observe o próximo exemplo:
v = d5.copy()
v[2] = 'novo valor'
print(v) #{1: 'a', 2: 'novo valor', 3: 'c'}
print(d5) #{1: 'a', 2: 'b', 3: 'c'}
#apesar dele criar uma cópia, ele não faz isso de maneira autentica. ele ainda referência o dicionario d5

#PARA CRIAR UM DICIONARIO COPIADO e cada um ser independente usamos o modulo import copy
import copy

d6 = { 1:'a', 2:'b', 3:'c'}
k  = copy.deepcopy(d6) # o deepcopy só é permitido com o modulo copy

lista = [
        ['abc',1],
        ['pqr',2],
        ['azd',3],
]

d1 = dict(lista)  #convertendo uma lista para um dicionario, é importante que ele esteja no padrao dicionario
print(lista)  #[['abc', 1], ['pqr', 2], ['azd', 3]] #lista
print(d1)  # {'abc': 1, 'pqr': 2, 'azd': 3} #dicionario

# para eliminar uma chave de um dicionario podemos usar o POP
d7={1:2,2:3,3:4,'p':89}
d7.pop('p') #eliminei a chave 'p'
print(d7) #{1: 2, 2: 3, 3: 4}

# para eliminar a ultima chave independente do nome
d7.popitem()
print(d7) #{1: 2, 2: 3}

#caso eu queria juntar dois dicionarios posso usar update
d7.update(d6)
