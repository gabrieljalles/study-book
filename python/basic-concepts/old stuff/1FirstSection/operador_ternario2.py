"""
operador ternário em python
"""

idade = 17

if idade >= 18:
    print('pode acessar.')
else:
    print("Não pode acessar.")
#==================================================
#simplificando
idade = input("qual a sua idade")

if not idade.isnumeric():
    print("você precisa digitar apenas numero")
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = 'pode acessar' if e_de_maior else 'não pode acessar'
    print(msg)
