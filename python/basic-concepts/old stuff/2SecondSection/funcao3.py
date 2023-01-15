"""
*args **kwargs  pode ser qualquer nome, mas por convensão usa-se args e kwargs
"""
#quando você já coloca um argumento padrão na variável, caso chame a funcao sem passar nenhum argumento, eles serão usados

def funcao(msg='olá senhor',nome='usuario'):
    nome=nome.replace('e','3') # replace é usado para substituir um valor por outro no argumento passado
    print(msg,nome)
funcao() #observe que mesmo sem digitar nada, ele aceitou a funcao.
funcao('meu nome é','cleiton pinto') # veja que colocando argumento também funciona
