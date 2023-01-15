texto = 'python'
c = 0
while c < len(texto):
    print(texto[c])
    c+=1
#  equivalente a isso,  usando o for, olha como é mais rápido
# para cada elemento (com nome letra), dentro do texto, digite letra.
for letra in texto:
    print(letra)

#função range(start = 0, stop, step=1)
# para cada n no range de 10 imprima o número Resposta = 0 1 2 3 4 5 6 7 8 9
for n in range(10):
    print(n)

for k in range(5,10): # ele é inclusivo no 5 e exclusivo no 10 Resposta =  5 6 7 8 9
    print(k)

# por padrão, o step é 1, um em um. Resposta = 0 2 4 6 8 10 12 14 16 18
for p in range(0,20,2): # como coloquei o step 2, o algoritmo anda de dois em dois
    print(p)

for z in range (20,9,-1): #eu quero que o for me mostre os números de 20 a 10, quando tende ao negativo, preciso mostrar pro step que  ele é negativo
    print(z) # se eu quero mostrar o  10 então preciso colocar nove no segundo argumento, uma vez que ele é exclusivo.
