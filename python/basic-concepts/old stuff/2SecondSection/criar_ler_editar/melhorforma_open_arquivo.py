#gerenciador de conxtexto em python
 # essa é a melhor forma pq não preciso fechar o arquivo

with open ('abc.txt','w+') as file:
    file.write('linha 1\n')
    file.write('linha 2\n')
    file.write('linha 3\n')
    file.write('linha 4\n')

    file.seek(0)
    print(file.read())
