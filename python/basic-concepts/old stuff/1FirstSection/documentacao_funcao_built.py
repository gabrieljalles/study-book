num1 = input('digite um número')
num2 = input('digite outro número')

"""
muitas vezes você precisa verificar se um usuário digitou realmente o valor esperado, no caso do num1, estamos esperando
um número. Ele pode simplismente digitar uma letra e quebrar o código. Sabemos que o input volta type string.
Por mais que seja do tipo string, precisamos verificar se foi digitado um número realmente. Por isso é importante que
conhecer a documentacao build in https://docs.python.org/3/library/stdtypes.html
Após pesquisar, vemos que 3 opções nos são favoraveis.
isdecimal() = retora true se todos os caracteres são decimais.
isdigit() = retorna true se todos os caracteres da string são digitos
isnumeric() = retorna true se todos os caracteres são números e posítivos (123456)
"""

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print(num1+num2)
else:
    print("digite apenas números para realizar a soma")

"""
Existe também o try e o except que é muito semelhante ao if e else, só que ele passa a ideia de tente esse, 
se não der, tente outro. Evita do código ser quebrado.
"""
try:
    num1 = float(num1)
    num2 = float(num2)
except:
    print("ERROR")


