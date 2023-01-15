#lembre que é preciso baixar o requests pip install requests
#lembre que é preciso baixo o Beautifulsoup beautifulsoup4 provavelmente esse 4 pode bugar no futuro

import requests #baixa o html
from bs4 import BeautifulSoup #permite que trabalhamos com a html no próprio python

url = 'https://pt.stackoverflow.com/questions/tagged/python'
response = requests.get(url)
#print(response.text) #html completo sem tratamento
html = BeautifulSoup(response.text, 'html.parser')#tratando...


for pergunta in html.select('.s-post-summary'):   # mostrando pro python o padrao de perguntas
    titulo = pergunta.select_one('.s-link')  # pegando apenas o titulo de cada pergunta na pagina
    data = pergunta.select_one('.relativetime')  # pegando apenas a data
    print(data.text, titulo.text, sep ='\t') #colocando uma tubulação
