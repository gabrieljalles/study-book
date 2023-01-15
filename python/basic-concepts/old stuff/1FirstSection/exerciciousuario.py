usuario = input("digite seu nome de usuario")

if usuario.isalpha():
    if len(usuario) <= 5:
        print("seu usuario tem menos que 5 letras digite algo maior")
    elif len(usuario)>=6 and len(usuario)<=8:
        print("seu usuario tem a segurança boa")


else:
    print("digite apenas letras")



