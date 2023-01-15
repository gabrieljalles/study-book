# todas as exceções do python
#https://docs.python.org/3/library/exceptions.html

# criando as próprias exceções
def divide(n1,n2):
    if  n2 == 0:
        raise ValueError("n2 não pode ser 0") # o raise é usado para levantar sua própria exceção
    return n1/n2

#agora vamos tratar a exceção criada
try:
     print(divide(2,0)) # nesse caso aparece o erro ZeroDivisionError
except ValueError as error:
    print(error)

#==========================================================
#usando try_except como condicional:

def converte_numero(valor):
    try: # ela tentar transformar o número em inteiro
        valor = int(valor)
        return valor

    except ValueError:
        try: # ela tenta transformar em float
            valor = float(valor)
            return valor
        except ValueError: # ele retorna none caso nenhum das opções acima é respeitada
            pass

numero = converte_numero(input("Digite um número:"))

if numero is not None:
    print(numero* 5)
else:
    print('isso não é número')
