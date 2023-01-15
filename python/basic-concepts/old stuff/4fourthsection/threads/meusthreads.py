# você consegue dividir os processos para que o varios processos sejam executados ao mesmo tempo

from time import sleep
from threading import Thread
from threading import Lock

# ---------------1  forma de trabalhar com thread ------------------------------------------------------------
"""class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo
        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)


t1 = MeuThread('thread1', 5)
t1.start()

t2 = MeuThread('thread 2', 8)
t2.start()

t3 = MeuThread('thread 3', 10)
t3.start()

for i in range(20):
    print(i)
    sleep(1)
"""

# --------------2 forma de trabalhar com thread -------------------------------
"""
def demora(texto, tempo):
    sleep(tempo)
    print(texto)


t = Thread(target=demora, args=('olá mundo', 5))
t.start()

t1 = Thread(target=demora, args=('olá mundo  1', 8))
t1.start()

t2 = Thread(target=demora, args=('olá mundo  2', 4))
t2.start()

for i in range(20):
    print(i)
    sleep(1)
"""
# ---------------------------------------------------------------------------
# Existe algumas maneiras de mandar status de um processo acontecendo
"""
def demora(texto, tempo):
    sleep(tempo)
    print(texto)

t2 = Thread(target=demora, args=('olá mundo  2', 4))
t2.start()

while t2.is_alive():
    print('Esperando acontecer a thread')
    sleep(3)
else:
    print('Thread executada com sucesso !')
    
"""


# ---------------------------------------------------------------
# varias pessoas podem tentar comprar ao mesmo tempo um mesmo ingresso !

class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire() # trancando o banheiro por dentro
        if self.estoque < quantidade:
            print("ingressos esgotados !")
            self.lock.release() # destrancnado o banheiro
            return

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingressos. Ainda temos {self.estoque}')
        self.lock.release() # destrancando o banheiro


if __name__ == '__main__':
    ingressos = Ingressos(10)

    threads = []
    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        threads.append(t) #colocando as threads na lista para executar tudo ao mesmo tempo

    for t in threads:
        t.start()


    executando = True #CRIEI UMA VARIAVEL ASSUMINDO QUE TUDO JÁ ESTÁ EXECUTANDO, PARA LIGAR O WHILE SEM PENSAR
    while executando:
        executando = False # AGORA DIGO QUE O EXECUTANDO É FALSE

        for t in threads: # E PERGUNTO SE EXISTE ALGUMA THREAD EM EXECUCAO
            if t.is_alive():# SE SIM....
                executando = True # DEIXE EXECUTANDO TRUE, REPITA O PROCESSO
                break

# ANTES DE MOSTAR OS INSGRESSOS, ESTOU CONFIRMANDO SE NÃO EXISTE NENHUMA THREAD ABERTA
    print(ingressos.estoque)