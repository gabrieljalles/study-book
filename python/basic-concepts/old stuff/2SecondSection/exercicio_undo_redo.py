"""
Faça uma lsita de tarefas com as seguintes opções:
adicionar tarefa
listar tarefas
opção de desfazer ( a cada vez que chamada, deve apagar a ultima tarefa adicionada)
opção de refazer ( a cada vez que chamada, deve adicionar novamente a tarefa  apagada)
"""
lista_de_tarefas = ['tarefa1','tarefa2','tarefa3']
contador = 0
lixeira = []
def acoes():
    resposta = input('qual ação você deseja fazer ? adicionar,desfazer ou refazer ?')
    global contador
    global lixeira
    if resposta == 'adicionar':
        adicao = input("qual o nome da tarefa que quer adicionar ?")
        lista_de_tarefas.append(adicao)
    elif resposta == 'desfazer':
        contador += 1
        lixeira.append(lista_de_tarefas[-1])
        lista_de_tarefas.pop()

    elif resposta == 'refazer':
        if contador >= 1:
            lista_de_tarefas.append(lixeira[-1])
            lixeira.pop()
            contador -= 1
        else:
            print("não existe tarefas para serem recolocadas")
    else:
        print("digite um valor válido")
while True:

    print(f'sua lista de tarefas atual :\n\t{lista_de_tarefas}') #antes da modificacao

    acoes()

    print(lista_de_tarefas)
    nova_atividade = input('deseja continuar modificando? [s]im ou [n]')

    if not nova_atividade == 's':
        print(f'sua lista final ficou {lista_de_tarefas}')
        break
    else:
        continue

