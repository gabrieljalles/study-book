import math

PI=math.pi  # no python, caso queira criar uma constante, que não muda seu valor. variavel em maiuscula

lista = [1,2,3,4,5]

def dobra_lista(lista):
    return [x*2 for x in lista]

print(dobra_lista(lista))

def multiplica_valores_lista(lista):
    r=1
    for x in lista:
        r*=x
    return r
print(multiplica_valores_lista(lista))

#vamos dizer que eu não quero que algo seja passado para outro modulo, mas quero que continue aqui
"""
se digitarmos print(__name__) aqui nesse código, ele aparece "__main__" mas se digitarmos esse mesmo código
puxando de outro lugar, irá aparecer o nome desse código ao ínvés de main.
dessa forma, o código abaixo, força a digitar coisas específicas para o ESTA  "pasta"
"""
if __name__ == '__main__':
    print("faça tal coisa somente para esse código")