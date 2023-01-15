"""
str - string
int - inteiro - 123 -5 -65
float - real/ponto flutuante - 1.5 10.50 -10.10
bool - booleano/lógico - 10 == 10  - true/false
"""
# para saber se o tipo de um dado, use type, observe:
print(10, type(10))  # int
print("feijao", type("feijao"))  #string
print(25.3, type(25.3))  #float
print(10==10, type(10==10))  #boolean, se existir qualquer valor no campo, ele pode ser considerado true, e caso esteja vazio, false

print(bool(''))  # false
print (bool('qualquer coisa')) # true
