"""
for/ else em python
"""
  # assim como o while tem break e continue, o for também tem.
variavel = ['luiz otavio','Joaozinho','maria']

for elemento in variavel:
    print(elemento)
    continue
    print(elemento)  # não aparece duas vezes pq o continue volta # o for sem perder o caminho

  #existe um comando startswith('') que diz, se começa com tal letra faça isso, veja o exemplo
for valor in variavel:
    if valor.startswith('j'):
        print(f' {valor} começa com j')
    else:
        print(f'{valor} não começa com j')
print("=================================================================================================")
"""
existe um problema em que o startswith só confere exatamente o valor expresso, se o valor da lista variável começar com maiuscula,
ele não identifica, para consertar esse problema, precisamos, antes de conferir se existe algum valor que começa com (''),precisamos
passar ele pra minuscula dessa forma :
    .lower()
"""
comeca_com_j = False
for valor in variavel:
    if valor.lower().startswith('j'):  #OBSERVE que o j do jãozinho é maiuscula, e o j da questão é minuscula e mesmo assim funciona.
        comeca_com_j = True     #anteriormente o algoritmo disse que não identificou nenhum e agora identificou. problema resolvido
if comeca_com_j:
    print('Existe uma palavra que começa com j.')
else:
    print('Não existe uma palavra que começa com J')

""" assim como no while, eu tambem posso usar o else aqui , observe que o código irá ser exibido menor"""
print("=================================================================================================")
for valor in variavel:
    if valor.lower().startswith('j'):
        print("existe um valor que começa com a letra j")
        break
else: #quando o laço é forçado a ser quebrado, o else não é executado.
    print("não existe uma palavra que começa com j")