import documentacao

help(documentacao)

"""
NAME
    documentacao - Antes do modulo começar, é importante dizer o que ele faz de maneira rápida na primeira linha (xxxxxxx)

DESCRIPTION
    pula uma linha e faz uma descrição completa dizendo todas as funções de maneira completa

FUNCTIONS
    multiplica(x, y, z=None)
        Multiplica x, y, z
        
        Multiplica x,y e z. O programador por omitir a variável z caso não tenha necessidade de usa-la

"""

# se eu quero chamar um help somente da funcao

help(documentacao.multiplica)


# DOCUMENTACAO CLASSE
class MinhaClasse:
    """Documentacao curta

    documentacao longa]
    """

    def __init__(self, texto):
        """inicializa texto

        :param texto: o texto da classe
        :type texto: str
        """

    def exibe_texto(texto):
        """
        metodo que exibe um texto de 100 caracteres

        :param texto: texto 100 caracteres
        :type texto: str

        :return: text 100 caracteres
        :rtype: str

        :raises ValueError: Se  o texto tiver de mais que 100 caracteres
        :raises TypeERROR: Se texto não for string
        """
        if is not isinstance?(texto, str):
            raise typeError('texto precisa ser string')

        if len(texto) > 100:
            raise ValueError('texto precisa ter 100 caracteres ou menos ')

        return texto

#outras praticas que ajudam na programação

x: int = 10 #dizer na própria variavel o tipo para facilitar a vida de todos
def funcao(p1: float,p2: str)-> float:# dizer logo de início o que é cada parametro recebe e o que retorna ->

#caso a sua funcao volta 2 valores distintos:
# dessa forma, facilita muito para outros desenvolvedores
from typing import Union
def funcao() -> Union[list,dict]:
    return []

