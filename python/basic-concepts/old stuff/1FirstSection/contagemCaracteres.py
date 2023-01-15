usuario = input('Digite seu usuário:')
qtd_caracteres = len(usuario)
# o len já retorna a quantidade de caracteres em INTEIRO
# é possível realizar calculos com ele.
print(usuario,qtd_caracteres,type(qtd_caracteres))

if qtd_caracteres < 6 :
    print('você precisa digitar pelo menos 6 caracteres')
else:
    print("voce foi cadastrado no sistema")

