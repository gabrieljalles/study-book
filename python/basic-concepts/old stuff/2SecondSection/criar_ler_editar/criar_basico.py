#Antes de mais nada,  é importante dizer que as importações devem ser levadas em consideração o arquivo principal
#Mesmo estando em outros arquivos

# 'r' open for reading
# 'w' open for writing, truncating the file first  escreve o arquivo e sobrescreve ele
# 'x' open for exclusive creationg, failing if the file already exists
# 'a' open for writing, appending to the end of the file if it exists ele adiciona texto ao arquivo,não sobrescreve ele
# 'b' binary mode
# 't' text mode
# '+' open a disk file for updating( reading and writing)

file = open('abc.txt', 'w+') #escrever e ler
file.write('linha 1\n')
file.write('linha 2\n')
file.write('linha 3\n')


file.seek(0,0) # buscar a posicao absoluta no arquivo
print('lendo linhas:')
print(file.read())
print('-------------------------')

"""
Se eu estou interessado em abrir o arquivo com ele aberto, devo me atentar que quando eu peço para ele fazer algo o cursor se movimenta
devo colocar ele novamente no zero absoluto para ler novamente. se eu quisesse ler ele com ele fechado não precisaria fazer isso.
por isso que  quando digitei file.read() não apareceu nada. Para arrumar isso, file.seek(0,0) para colocar o ponteiro no inicio

"""

file.seek(0,0)
print(file.readline(),end='') #ler linha por linha
print(file.readline(),end='') #ler a próxima linha

#-------------------------
"""
terminal 1  :
linha 1

linha 2

por padrão ele manda uma quebra de linha na leitura, ou seja, uma querba por \n e outra automatico. para arrumar a quebra
automatica, basta colocar o padrão end=''

terminal com end='':
linha 1
linha 2
"""
#-------------------------


file.close() # é muito importante fechar o arquivo após usa-lo
# quando eu executei ele criou o arquivo

import os # para remover arquivo
os.remove('abc.txt')


