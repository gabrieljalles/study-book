"""
condicoes if, elif e else - aula 4
"""
# a convensão em python é usar 4 espaços para mostrar que um texto é filho de outro OU TAB

bool = True
if bool:  #nesse caso, já estou dizendo que é verdadeiro, então ele sempre escreve o texto.
    print("verdeiro.")
elif True:  #caso tenha mais alguma coisa para testar que não seja aceita na linha acima, o código irá procurar do elif
    print(" agora é verdadeiro")
else:  # caso não seja verdadeiro em nenhum caso,  ele executa as linhas de baixo, ela depende da expressão if, NÃO funciona sozinha.
    print("falso.")

# == > >= < <= !=
# sempre que usar um sinal de igual então estou afirmando, se usar dois sinais de igual,então estou perguntando

print(2 == 2)
#===================================================
nome = input("qual seu nome  ? ")
idade = input ("qual sua idade ? ")

#minimo para pegar um empréstimo
idade_minima = 18
#maximo para pegar um empréstimo
idade_maxima = 30


if int(idade) >= idade_minima and int(idade)<=idade_maxima:
    print(f'{nome} pode pegar um emprestimo')
elif int(idade)<=idade_minima :
    print(f'{nome} você é muito jovem para pegar um empréstimo')
elif int(idade)>=idade_maxima :
    print(f'{nome} você já ta com o pé na cova, não queremos prejuízo.')









