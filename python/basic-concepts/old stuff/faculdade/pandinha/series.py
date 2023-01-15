import pandas as pd


def p(*wargs):
    print(*wargs)


# construir um objeto do tipo series
# = pd.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)

# Parametros
"""
data: informação armazenada nas series, aceita dict, array, iterable, valor escalado

index: uma forma de indexar cada linha, por padrão (None) é 0,1,2... caso seja passado um dict, as chaves passam a ser o indice

dtype: str, numpy.dtype, or extensiondtype, opcional. pode dizer quantos dados cada elemento aceita exe: int64

name: str, opcional

copy: bool, default false . 
"""

d = {'a': 1, 'b': 2, 'c': 3}

t = pd.Series(data=d, index=['a', 'b', 'c'])
print(t)

"""
a    1
b    2
c    3
dtype: int64
"""

# caso os valores sejam diferente da chave, o series não tem efeito
t = pd.Series(data=d, index=['x', 'y', 'z'])
print(t)

"""
a    Nan
b    Nan
c    Nan
dtype: int64
"""

k = pd.Series(data=5)  # observe que por padrão, há um indice
print(k)
"""
0   5
"""
lista_nomes = 'jalles gabriel fernanda brenda luiza'.split()
print(pd.Series(lista_nomes))
"""
0      jalles
1     gabriel
2    fernanda
3      brenda
4       luiza
dtype: object
"""

cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()
dados = pd.Series(lista_nomes, index=cpfs)
"""
111.111.111-11      jalles
222.222.222-22     gabriel
333.333.333-33    fernanda
444.444.444-44      brenda
555.555.555-55       luiza
dtype: object
"""
# posso saber o nome da pessoa pegando pelo indice .loc[]
p(dados.loc['111.111.111-11'])  # resposta: Jalles

# Extraindo informacoes de uma serie
dados_series = pd.Series([10.2, -1, None, 15, 23.4])
p('Quantidade de linhas = ', dados_series.shape) # .shape mostra a QTD  linhas
p('Tipo de dados = ', dados_series.dtypes) # Retorna o tipo de dados, se for mistro será object
p('Os valores são unicos ? ', dados_series.is_unique) # verifica se não há duplicações
p('Existem valores nulos ? ',dados_series.hasnans)
p('Quantos valores existem ? ',dados_series.count()) # RESP 4 : ele não conta o None
p('qual o menor valor ? ',dados_series.min())
p('qual o maior valor ?', dados_series.max())
p('Qual a media aritmetica?', dados_series.mean())
p('Qual o desvio padrão ? ', dados_series.std())
p('Qual a mediana?', dados_series.median()) # Extrai a mediana de uma serie numérica

p('\nResumo: \n', dados_series.describe()) # fala tudo acima em uma linha
