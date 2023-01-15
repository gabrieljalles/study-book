import csv

with open('teste.csv','r') as arquivo:
    dados = csv.reader(arquivo)
#caso eu não queira que a primeira linha não apareça, a linha do cabecalho:
    #next(dados) # só é possível por ser um iterador
    print(dados) #iterador : <_csv.reader object at 0x000002013A63AD40>

#para converter para dicionario:
    dados = csv.DictReader(arquivo)

    for dado in dados:
        print(dado)
        print(dado['nome']) # quaro um elemento especifico desde que seja um DICIONARIO

#para abrir o arquivo fora do with, ou seja com ele fechado:
#use list comprehension
with open('teste.csv','r') as arquivo1:
    dados = [x for x in csv.DictReader(arquivo1)]

#veja que mesmo não identado posso chama-lo
for dado in dados:
    print(dado)

#passando de um arquivo para o outro:
#teste para teste2


with open('teste2.csv','w') as arquivo:

    escreve = csv.writer(
        arquivo,
        delimiter=',', #arquivo separado por virgula
        quotechar='"', #qual caractere é usado , recomenda usar o aspas duplas
        quoting=csv.QUOTE_ALL #estou pedindo para o arquivo colocar aspas em todos os meus dados
     )
    chaves = dados[0].keys()
    chaves = list(chaves)
    escreve.writerow(
        [
            chaves[0],
            chaves[1],
            chaves[2],
            chaves[3],

        ]
    )

    for dado in dados:
        escreve.writerow(
            [
                dado['nome'],
                dado['sobrenome'],
                dado['email'],
                dado['numero'],
            ]
        )






