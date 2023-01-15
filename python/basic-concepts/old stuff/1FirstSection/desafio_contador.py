contador_a = 0
contador_r = 10

while contador_a<10 and contador_r>0:
    print(contador_a,contador_r)
    contador_a += 1
    contador_r -= 1
    if contador_r < 2  and contador_a > 8:
        break
print('==========Outra forma =================================')
for p, r in enumerate(range(10,1,-1)):
    print(p,r)



