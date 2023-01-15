"""
escopo global e local
========================
um erro que não pode acontecer, você não pode mesclar vairaveis globais  e modifica-las localmente e depois usa-las

variavel="valor"

def func():
    print(variavel) VOCÊ NÃO PODE USAR A GLOBAL...
    variavel = 12345 MODIFICAR...
    print(variavel) E DEPOIS USAR A LOCAL , O PYTHON IGNORA A GLOBAL E DIZ QUE VOCÊ ESTÁ TENTANDO USAR ANTES DE CRIA-LA
"""

variavel = 'valor'

def func():
    outro_valor = variavel
    return outro_valor

def func2(arg):
    print(arg)

var = func()
func2(var)
