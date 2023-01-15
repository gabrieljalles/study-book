"""
Operador ternário em Python
"""
logged_user = True

if logged_user:
    msg = 'Usuário logado'
else:
    msg = 'Usuário precisa logar'

print(msg)

#================================================
#deixando o coódigo menor
msg= 'usuario logado testando.' if logged_user else 'usuário precisa logar.'
print(msg)

