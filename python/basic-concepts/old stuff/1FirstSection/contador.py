contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    acumulador = acumulador + contador
    contador +=1
# a utilização de else em comando de while, diz que quando  a condição deixar de ser verdadeira, ele executa o else.
#algumas o looping acaba mesmo a condição não acabando por inteira, como por exemplo a utilização de break; então o while acaba, mas o else não executa
else:
     print("cheguei no else, ou seja o while é falso")
print("o while acabou mas o else não foi completado, ou seja, o while foi quebrado antes da finalização")
