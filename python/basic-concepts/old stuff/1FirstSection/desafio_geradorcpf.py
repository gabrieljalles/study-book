cpf_digitado = input('digite seu cpf')

#cpf_digitado = "16899535055"

#Conferir se o cpf atende as especificações minimas para ser um cpf possívelmente válido
if cpf_digitado.isnumeric() and len(cpf_digitado) == 11:

#variáveis de auxílio:
    somatorio = 0
    somatorio_2 = 0
    k = 10

    for i in cpf_digitado:
        i = int(i)
        temporario = i * k
        somatorio += temporario
        k-=1
        if k == 1:
            k=10
            break

    digito_1 = (11-(somatorio%11))
    if digito_1 > 9:
        digito_1 = 0
    print(f'{somatorio} digito 1 é igual a {digito_1}')

    for i in cpf_digitado:
        i = int(i)
        temporario = i * (k+1)
        somatorio_2 += temporario
        k-=1
        if k == 1:
            somatorio_2 = somatorio_2 + (digito_1*2)
            break


    digito_2 = (11-(somatorio_2%11))
    print(f'{somatorio_2} digito 2 é igual a {digito_2}')

    #Agora irá ter a confirmação se o cpf digitado  é valido ou não
    c=0
    acumulador_cpf = ''
    while c < 9:
        acumulador_cpf += cpf_digitado[c]
        c+=1
    digito_1 =str(digito_1)
    digito_2 =str(digito_2)

    cpf_novo = acumulador_cpf + digito_1 + digito_2

    cpf_aceito = cpf_digitado == cpf_novo
    mensagem_conferencia =  'o seu cpf foi aceito com sucesso.' if cpf_aceito else 'infelizmente seu cpf não é valido.'
    print(mensagem_conferencia)

else:
    print('O programa só aceita números e um cpf válido tem apenas 11 digitos')


