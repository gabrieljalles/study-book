from classes import * # não recomendado fazer isso, importa tudo

c1 = Cliente('LUIZ', 45)
print(c1.nome)
a1 = Aluno('Maria',32)
print(a1.nome)

a1.falar() # Aluno está falando
c1.falar() # Cliente está falando
c1.comprar()
a1.estudar()