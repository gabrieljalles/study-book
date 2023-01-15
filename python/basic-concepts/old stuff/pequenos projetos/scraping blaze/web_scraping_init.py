import requests
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# ---------------------------------------------------------------------------------
"""
Modulo com objetivo de realizar atividades básicas do web-scrapping:
    Abrir chrome
    entrar no site
    sair do site
"""
# ---------------------------------------------------------------------------------


# Criando classe chrome
class ChromeAuto:

    def __init__(self):
        self.driver_path = 'chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('chromedriver.exe')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def acessa_site(self,site):
        self.chrome.get(site)

    def exit(self):
        self.chrome.quit()

# lembrar de separar essa func no modulo blaze
    def procura_valores_blaze(self):
        try:
            valor = self.chrome.find_element(By.CLASS_NAME, "entries").text
            return valor
        except Exception as e:
            print('Erro ao procurar valor:', e)

#PROVISORIO
    def exibe_lista(self,valor):
        for x in valor:
            lista.append(x)
        while n in lista:
            lista.remove(n)
            lista.remove(x)
        print(lista)

"""
ANOTAÇÕES:
    Consegui  capturar no blaze os valores, meu objetivo agora é colocar eles em uma lista
    Estou tentando juntar os valores assim [1.82,1.45...]   
    Parei tentando criar uma funcao exibe_lista que, além de exibir, formata ela do jeito que eu quero
"""


