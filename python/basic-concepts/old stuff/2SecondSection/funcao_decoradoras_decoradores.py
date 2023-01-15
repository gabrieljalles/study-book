from time import time
from time import sleep

# fazendo uma funcao que aceita outras funcoes para saber quanto tempo elas demoram para executar

def velocidade(funcao): # a funcao velocidade recebe uma funcao
    def interna(*args,**kwargs): # a funcao velocidade tem uma funcao interna que recebe parametros aleatórios
        start_time = time() # captura o tempo antes de começar o código
        resultado = funcao(*args,**kwargs)  # essa funcao interna retorna e ativa a funcao recebida
        end_time  = time() # captrua o tempo depois de acabar o código
        tempo = (end_time - start_time) # tempo que levou para executar a funcao
        print(f' a função{funcao.__name__} levou {tempo} segundos para executar.') # delta do tempo
        return resultado # retorna o resultado para a funcao interna
    return interna # a funcao velocidade retorna a funcao interna sem executar


@velocidade
def demora(): # FUNCAO QUALQUER PARA SER DECORADA
    for i in range(10):
        print(i)
        sleep(1)


demora()


