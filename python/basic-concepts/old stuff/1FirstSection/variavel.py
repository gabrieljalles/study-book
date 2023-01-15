"""
Uma variável se inicia sempre com uma letra, pode conter números e para separar usar _, letras minúsculas
"""
nome = 'Luiz Otávio'
idade = 32
altura = 1.8
e_maior = idade > 18
data_atual = 2019
data_1 = True  # a primeira letra do bool explicito precisa ser Maiusculo
peso =  80
imc = peso/(altura ** 2)


print('nome:',nome)
print('idade',idade)
print('altura',altura)
print('é maior',e_maior)
print(nome,"tem", idade, "anos de idade e seu imc é", imc)

#outra forma de montar essa  mensagem use (f'....
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')  # .2f significa que eu quero somente com duas casas decimais

#outra forma
print('{} tem {} anos de idade  e seu imc é {:.2f}'.format(nome,idade,imc))