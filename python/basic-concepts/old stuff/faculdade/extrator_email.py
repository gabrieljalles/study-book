dados_1 = {
    'nome': ['Sonia Weber', 'Daryl Lowe', 'Vernon Carroll', 'Basil Gilliam', 'Mechelle Cobb', 'Edan Booker',
             'Igor Wyatt', 'Ethan Franklin', 'Reed Williamson', 'Price Singleton'],
    'email': ['Lorem.ipsum@cursusvestibulumMauris.com', 'auctor@magnis.org', 'at@magnaUttincidunt.org',
              'mauris.sagittis@sem.com', 'nec.euismod.in@mattis.co.uk', 'egestas@massaMaurisvestibulum.edu',
              'semper.auctor.Mauris@Crasdolordolor.edu', 'risus.Quisque@condimentum.com',
              'Donec@nislMaecenasmalesuada.net', 'Aenean.gravida@atrisus.edu'],
    'enviado': [False, False, False, False, False, False, False, True, False, False]
}

dados_2 = {
    'nome': ['Travis Shepherd', 'Hoyt Glass', 'Jennifer Aguirre', 'Cassady Ayers', 'Colin Myers', 'Herrod Curtis',
             'Cecilia Park', 'Hop Byrd', 'Beatrice Silva', 'Alden Morales'],
    'email': ['at@sed.org', 'ac.arcu.Nunc@auctor.edu', 'nunc.Quisque.ornare@nibhAliquam.co.uk', 'non.arcu@mauriseu.com',
              'fringilla.cursus.purus@erategetipsum.ca', 'Fusce.fermentum@tellus.co.uk', 'dolor.tempus.non@ipsum.net',
              'blandit.congue.In@libero.com', 'nec.tempus.mauris@Suspendisse.com', 'felis@urnaconvalliserat.org'],
    'enviado': [False, False, False, True, True, True, False, True, True, False]
}



def extrair_lista_email(dict_1, dict_2):
    lista_1 = list(zip(dict_1['nome'], dict_1['email'], dict_1['enviado']))
    lista_2 = list(zip(dict_2['nome'], dict_2['email'], dict_2['enviado']))

    dados = lista_1 + lista_2

    email_nao_enviados = [x[1] for x in dados if not x[2]]

    return email_nao_enviados


email_nao_enviados = extrair_lista_email(dados_1, dados_2)
print(email_nao_enviados)
