import pandas as pd

pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)

lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()
lista_cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()
lista_emails = 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split()
lista_idades = [32, 22, 25, 29, 38]

print(pd.DataFrame(lista_nomes, columns=['nome'], index=lista_cpfs))  # indexando ao cpf

dados = (list(zip(lista_idades, lista_emails, lista_cpfs, lista_nomes)))
print(pd.DataFrame(dados, columns=['idade', 'email', 'cpf', 'nomes']))

#dataframe podem ser criados com dicionario;
#chaves serão o nome da coluna e os valores precisam ter sempre a mesma quantidade

dados = {
    'nomes': 'Howard Ian Peter Jonah Kellie'.split(),
    'cpfs' : '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split(),
    'emails' : 'riisus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split(),
    'idades' : [32, 22, 25, 29, 38]
}

print(pd.DataFrame(dados))

#tirando informarcoes do dataframe
df_dados = pd.DataFrame(dados)
print('\nInformacoes do DATAFRAME:\n')
print(df_dados.info()) #informacoes tecnicas do dataframe

print('\nQuantidade de linhas e colunas = ', df_dados.shape) # Retorna uma tupla com o número de linhas e colunas
print('\nTipo de dados:\n', df_dados.dtypes) # Retorna o tipo de dados, para cada coluna, se for misto será object

print('\nQual o menor valor de cada coluna?\n', df_dados.min) # Extrai o menor de cada coluna
print('\nQual o maior valor?\n', df_dados.max()) # Extrai o valor máximo e cada coluna
print('\nQual a média aritmética?\n', df_dados.mean()) # Extrai a média aritmética de cada coluna numérica
print('\nQual o desvio padrão?\n', df_dados.std()) # Extrai o desvio padrão de cada coluna numérica
print('\nQual a mediana?\n', df_dados.median()) # Extrai a mediana de cada coluna numérica

print('\nResumo:\n', df_dados.describe()) # Exibe um resumo

df_dados.head() # Exibe os 5 primeiros registros do DataFrame

