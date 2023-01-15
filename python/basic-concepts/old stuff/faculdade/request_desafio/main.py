import requests
from datetime import datetime

dados = requests.get('https://servicodados.ibge.gov.br/api/v2/cnae/classes').json()

# quantidade distinta de atividades
qtd_atividades = len(dados)

# criar uma lista dos grupos de atividades, extraindo a descrição de cada registro
grupos = []
for registro in dados:
    grupos.append(registro['grupo']['descricao'])

qtd_grupos_distintos = len(set(grupos))

contador_grupo = [(grupo, grupo.count(grupo)) for grupo in set(grupos)]

# transformando a lista em dict
contador_grupo = dict(contador_grupo)

# agora, por meio do dicionario
print(contador_grupo)

valor_maixmo = max(contador_grupo.values())
grupo_mais_atividades = [chave for (chave, valor) in contador_grupo.items() if valor == valor_maixmo]

print(grupo_mais_atividades)


class ETL:
    def __init__(self):
        self.url = None

    def extract_cnae_data(self, url):
        self.url = url
        data_extracao = datetime.today().strftime("%Y/%m/%d  %H:%M:%S")

        # extraindo dados
        dados = requests.get(self.url).json()

        # Extrai os grupos dos registros
        grupos = []
        for registro in dados:
            grupos.append(registro['grupo']['descricao'])

        # cria uma lsita de tuplas (grupo, quantidade_atividades
        grupos_count = [(grupo, grupos.count(grupo)) for grupo in set(grupos)]
        grupos_count = dict(grupos_count)
        