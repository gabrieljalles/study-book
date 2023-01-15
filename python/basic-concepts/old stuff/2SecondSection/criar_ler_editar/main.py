# trabalhando com a criação de arquivos
# convertando  pra json um dicionario

import json

d1 = {
    'pessoa 1': {
        'nome': 'luiz',
        'idade': 25,
    },
    'Pessoa 2': {
        'nome': 'Rose',
        'idade': 30,
    },
}

d1_json = json.dumps (d1, indent=True)

with open('abc.json','w+') as file: #w+ escrever ou sobrescrever
    file.write(d1_json)


