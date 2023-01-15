"""
Funções (def) em python - return - aula 16
"""
def funcao(var):
    return var #toda vez que existe return, tudo abaixo dele não é processado. por isso usamos ele somente no final da funcao

variacao = funcao('testando um dois tres') #o return me permite retornar o valor da funcao pra fora dela,e nesse momento,
#estou atribuindo  o valor a variavel variacao

print(variacao) #testando um dois tres

def saudacao(msg,nome):
    print(msg,nome)

saudacao('seja muito bem vindo','gabriel')

def soma(n1,n2,n3):
    print(n1+n2+n3)

soma(1,2,3)

def aumentoperc(n1,percent):
    return n1*percent/100 + n1

aumento = aumentoperc(10,100)

print(aumento)

def fizzbuzz(n):
    if n % 5 == 0 and n % 3 == 0:
        return 'fizzbuzz'
    if n % 3 == 0:
        return 'fizz'
    if n % 5 == 0:
        return 'buzz'
    return n


print(fizzbuzz(0))





