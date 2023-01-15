import pandas as pd


def p(k):
    print(k)


p(pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json").head())

pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/cities.csv").head()

df_selic = pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json")
print(df_selic.info())

df_selic.drop_duplicates(keep='last', inplace=True)
p("------------------------------------------------------------")
from datetime import date
from datetime import datetime as dt

data_extracao = date.today()
df_selic['data_extracao'] = data_extracao
df_selic['responsavel'] = "Autor"

print(df_selic.info())
p(df_selic.head())
