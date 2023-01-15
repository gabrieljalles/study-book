from vendas.formata import preco

def acrescimo(valor,porcentagem,formata=False):
    r  = valor + (valor * porcentagem)/100

    if formata:
        return preco.real(r)
    else:
        return r

#formatado = return format.real(r) if format else return r
#msg= 'usuario logado testando.' if logged_user else 'usuário precisa logar.'

def desconto(valor,porcentagem,formata=False):
    r = valor - (valor * porcentagem)/100

    if formata:
      return preco.real(r)
    else:
        return r


# o parametro format começa com false e caso eu queira fazer a modificação para formatar para o real, basta passar true lá na outra pagina