from classes import Cliente
#Para compreender melhor execute o código, veja que se apagar o cliente 1 ele também apaga a cidade e estado, logo a cidade e estado depende do cliente 1
cliente1 = Cliente('Luiz', 32)
print(cliente1.nome)
cliente1.inserir_endereco('belo horizonte', 'MG')
cliente1.lista_enderecos()
del cliente1

print() #pular linha
#---------------------------------------------------
cliente2 = Cliente('Maria', 42)
print(cliente2.nome)
cliente2.inserir_endereco('Unai', 'MG')
cliente2.inserir_endereco('São Paulo', 'SP')
cliente2.lista_enderecos()

print() #pular linha
#---------------------------------------------------
cliente3 = Cliente('Joao', 19)
print(cliente3.nome)
cliente3.inserir_endereco('uberlandia', 'MG')
cliente3.lista_enderecos()

print() #pular linha
print("####################################################")
print("o próprio programa apaga o resultado depois de mostra-lo, ele só não mostrava antes. a func DEL (na pagina CLASSE) mostra isso ")

