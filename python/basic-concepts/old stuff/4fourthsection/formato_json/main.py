"""
JavaScript Object Notation - JSON
JSON (JavaScript Object Notation) é um formato de troca de dados entre sistemas
e programas muito leve e de fácil utilização. Muito utilizado por APIs

DUMPS / Dump
######################
Python          JSON
dict	        object
list, tuple	    array
str	            string
int, float  	number
True        	true
FALSE	        False
None	        null

LOADS / Load
######################
JSON	        Python
object	        dict
array	        list
string	        str
number (int)	int
number (real)	float
true	        True
false	        False
null	        None

"""
from dados import *
import json

list = [1, 2, 3, 4, 5, 6]

dados_json = json.dumps(list)
print(dados_json, type(dados_json))  # observe que o formato quando convertido é esse : [1, 2, 3, 4, 5, 6] <class 'str'>

dados_json = json.dumps(clientes_dicionario)
print(dados_json, type(dados_json)) # deixa de ser dicionario e passa a ser str

print(clientes_json) #observe que é uma string do json
dicionario = json.loads(clientes_json) # convertendo para o formato dicionário

print(dicionario)
for chave, valor in dicionario.items():
    print(chave, valor)

#convertendo um dicionario em um arquivo json, para quando eu quiser, poder abrir ele em qualquer lugar transformando-o em
#um dicionario novamente

with open('cliente.json', 'w') as arquivo:
    json.dump(clientes_dicionario,arquivo, indent=4) #nesse caso é DUMP #ident é usado para facilitar a leitura

#para fazer a leitura do arquivo, e armazenando em uma variável data
with open('cliente.json', 'r') as arquivo:
    data = json.load(arquivo)

