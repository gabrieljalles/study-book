"""
Exceções são erros que podem acontecer ao longo do código e parar ele.
o try e except consegue contornar isso
para tratar, basta eu envolver o erro no bloco try:
"""

try:
    print(a)
    # você pode tratar o erro que aconteceu  usando except
               #|
               #v
except (NameError,KeyError) as erro:  # você pode tratar dois erros ao mesmo tempo
        print('Erro',erro)
except IndexError as erro:
        print('error')
except Exception as erro: # quando o erro não está tratado ele traz pra k
        print('ocorreu um erro inesperado')

else:
    print("seu código foi executado com sucesso!")
finally: # se ocorreu ou não ocorreu um erro, o finaly  executa sempre, pode ser usado para fechar algo que foi aberto nos erros
    print("Finalmente.")





