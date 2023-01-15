"""
1- crie uma funcao1 que recebe uma funcao2 como parametro e retorne o valor da funcao2 executada
"""
def funcao2():
    return 'um valor aleatório qualquer'

def funcao1(arg):
    print(arg())

funcao1(funcao2)

"""
2- Crie uma funcao1 que recebe uma funcao2 como parametro e retorne o valor da funcao2 executada. Faca a funcao1 executar
duas funcoes que recebam um número diferente de argumentos.
"""

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'oi {nome}'

def saudacao(nome,saudacao):
    return f'olá {nome}, {saudacao}'


executando = mestre(fala_oi,'luiz')
print(executando)
executando2 = mestre(saudacao,'luiz',saudacao='bom dia')
print(executando2)
