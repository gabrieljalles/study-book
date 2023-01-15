"""
Entrada de dados
"""
nome = input("Qual o seu nome ? ")
idade = input ("Qual é sua idade? ")
print(f'seja muito bem vindo {nome} o tipo da variável é 'f'{type(nome)}')
print(f'{nome} tem {idade} anos')

# é importante ressaltar que todo tipo, mesmo que seja digitado numero, será do tipo STRING
# nesse caso, precisamos converter variáveis de um tipo em outro.
ano_atual = 2021
ano_nascimento = ano_atual - int(idade)  #veja que converti a string idade para int( ) digitando esse comando

print(f'{nome} nasceu no ano  {ano_nascimento}')





