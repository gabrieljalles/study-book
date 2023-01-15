# se aparece uma palavra e depois o ()  ele é considerado uma função;
# assim como no exemplo, print()

print(123456)
print('luiz','otávio')  # quando se coloca vários argumentos separados por virgulas, eles  serão apresentados com espaço
print('luiz','otávio', sep='-')  # o sep ele deixa eu escolher qual será o separador entre os argumentos
print('luiz','otávio', end="##") # o end  me permite  finalizar a frase com algo.

# se eu colocar o end, ele junta a frase atual com a de baixo.
print('luiz','otavio', end="")
print('luiz','gosta',end="")
#resposta (luiz otávio##luiz otavioluiz gosta)
         # esse primeiro luiz otávio, é da linha  7

# com o python voce pode definir novas funções com def, com o nome de funcao

def funcao():
    print('Hello World!')
funcao()

#você pode acrescentar variáveis no processo, mas precisa denomina-las = observe:
def funcao(msg):
    print(msg)
#quando for chamar a funcao, é necessário aplicar a variável
funcao('eu defini o significado de msg')




