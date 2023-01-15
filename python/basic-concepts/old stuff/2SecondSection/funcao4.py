def func(a1,a2,a3,a4,a5,nome=None):   #quando eu crio uma variável já préestabelecida com argumento none,se eu não usar não acontece nada
    print(a1,a2,a3,a4,a5,nome)        #mas me da a opção de usar quando eu quiser
                                      #a partir do momento  que atribuo uma variavel default "nome=none" depois dela só pode vir default
                                      #exemplo de erro: a4,a5=none,a6 <===== ERRADO
func(1,2,3,4,5,nome="Gabriel")        #observe que eu não coloco semente o argumento, mas a variavel tbm;

print('============================================================')
# UMA TUPLA NÃO PODE SER MODIFICADA - MAS PODE SER CONVERTIDA EM LISTA FACILMENTE
def funcao(*args): #o uso de asteristico* mostra que não sei quantos argumentos serão passados.
    print(args)
    print('primeiro da lista',args[0]) #acessando o primeiro valor da tupla
    print('último da lista',args[-1]) #acessando o último valor da tupla
    print(f'tamanho da lista{len(args)}') #o tamanho da tupla


lista = [1,2,3,4,5]
n1,n2,*n =lista  # estou desempacotando os primeiros valores e deixando os demais empacotados
print(n1,n2,n)
print(*lista,sep=' ') #nessa situação eu estou desempacotando tudo e separando por padrão espaço,mas pode colocar outro
print("========Observe que eles estão empacotados em tupla==========")
funcao(1,2,3,4,5)
