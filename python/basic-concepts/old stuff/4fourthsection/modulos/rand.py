import random
import string

# gera numero inteiro entre A e B
inteiro = random.randint(10, 20)

# gera numero aleatorio usando a funcao range()
inteiro = random.randrange(900, 1000, 10)  # 1000 exclusivo / de dez em dez

# gera numero float entre A e B
float = random.uniform(10, 20)

# gera numero float  entre 0 e 1
float2 = random.random()

print(float)
print(float2)
print(inteiro)



#sorteando nome
lista = ['gabriel', 'jack', 'jalles', 'luis', 'rebeca', 'regina', 'brenda']
sorteio = random.choice(lista)
print(sorteio)
#sorteando varios nomes / o mesmo nome pode ocupar varias posicoes
sorteios = random.choices(lista, k=3)
print(sorteios)
#sorteando varios nome/ o nome só pode ocupar UMA possibilidade
sorteiosU = random.sample(lista,k=2)
print(sorteiosU)
#para embaralhar a própria lista, o código é alterado:
random.shuffle(lista)
print(lista)




#gerador de senhas ALEATÓRIOS
letrasmaiscminusc = string.ascii_letters
letrasmaisc = string.ascii_uppercase
letrasminusc = string.ascii_lowercase
digitos = string.digits
caracteres = '!@#$%¨&*_-=+'
geral = letrasmaiscminusc + digitos + caracteres
senha = "".join(random.choices(geral, k=20))
print(senha)



