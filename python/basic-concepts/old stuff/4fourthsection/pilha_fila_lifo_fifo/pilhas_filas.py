"""
pilhas e filas
Pilha (STACK) - LIFO - last in, first out
    Exemplo: pilha de livros que são adicionadas sobre o outro
Fila (Queue) - FIFO - first in, first out.
    Exemplo: Fila de banco
    Filas podem ter efeitos colaterais em desempenho, porque a cada item alterado, todos os indices serão modificados
"""
from collections import deque
#------------------PILHA--------------------------
"""
livros = list()
livros.append('livro 1')
livros.append('livro 2')
livros.append('livro 3')
livros.append('livro 4')
livros.append('livro 5')
print(livros)
livros.pop() # RETIRA O ULTIMO DADO COLOCADO A LISTA
print(livros)
#------------------Trabalhando com fila------------

fila = deque()
fila.append('safadinha')
fila.append('gabriel')
fila.append('jalles')
fila.append('cleiton')
fila.append('fernando peçanha')
print(fila)
#para retirar  da fila
print(f'saiu: {fila.popleft()}')
print(f'saiu: {fila.popleft()}')
print(fila)
fila.extend('arthur mandioquinha carne arroz feijao'.split()) #adicionando varias pessoas ao mesmo tempo
print(fila)
"""
#você pode colocar uma fila para ter tamanho maximo:
fila1 = deque(maxlen=10)
fila1.extend([1,2,3,4,5,6,7]) # assim que o limite é alcançado o valor mais antigo é retirado
print(fila1)