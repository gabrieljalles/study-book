class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self,other): # ensinando a somar OS OBJETOS criados por mim
        novox = self.x + other.x
        novoy = self.y + other.y
        return Retangulo(novox, novoy) # estou criando um novo retangulo com a soma dos anteriores

    def get_area(self): # pegando a area do retangulo
        return self.x * self.y

    def __lt__(self, other): # ensinando a comparar se o retangulo é MENOR que outro
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 < a2:
            return True
        else:
            return False

    def __gt__(self, other): # ensinando a comparar se o retangulo é MAIOR que outro
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 > a2:
            return True
        else:
            return False

    def __eq__(self, other): # ensinando o python a comparar os dois retangulos para ver se são iguais
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False






r1 = Retangulo(10,20)
r2 = Retangulo(10,20)
r3 = r1 + r2
print(r3)
print(r2 > r1)
#Vamos dizer que agora, eu queira somar os dois objetos, preciso ensinar o python a identifica-los como somaveis
