from vendas.calcula_preco import acrescimo,desconto
from vendas.formata import preco  # funcao que muda o numero para real

preco_objeto = 89.95

preco_acrescido = acrescimo(valor=preco_objeto,porcentagem=50, formata=True)
print(preco_acrescido)

preco_desconto = desconto(valor=preco_objeto,porcentagem=50, formata=True)
print(preco_desconto)

print(preco.real(50))