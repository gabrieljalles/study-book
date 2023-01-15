"""iterar  strings nada mais é que passar por todos os elementos de uma string fazendo checkagem"""

frase = "o rato roeu a roupa do rei de roma"
tamanho_frase= len(frase) #para saber quantas letras tem a frase
contador = 0 # o contador é usado para correr o while
nova_string = '' # a nova string no primeiro momento é usado para não fazer modificações na frase inicial

input_usuario = input("qual letra deseja colocar maiúscula:")  #  a maquina pergunta  qual letra deixar em maiúscula

while contador < tamanho_frase: #enquanto o contador for menor que o tamanho da frase
    letra = frase[contador] # a letra corresponde a letra  da frase referente ao indice contador
    if letra == input_usuario: # se letra for igual a o que o usuário pediu para ficar em maiúscula
        nova_string += input_usuario.upper()  # ele soma a nova string  a letra que o usuário digitou com a função upper()
    else:
        nova_string += letra # caso contrário, ele simplismente continua o calculo
    contador += 1  # e soma +1 ao contador que está fazend papel de indice

print(nova_string) # quando o while acaba, ele imprime na tela



