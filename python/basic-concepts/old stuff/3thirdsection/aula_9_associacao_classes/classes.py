class Escritor:
    def __init__(self, nome):  # nesse caso, o construtor está fazendo papel de setter
        self.__nome = nome
        self.__ferramenta = None

    # --------------------MUITO IMPORTANTE ---------------------------
    # SE O ATRIBUTO É PRIVADO __*******, como acima,  você precisa criar pelo menos um GETTER para acessar ele fora da classe

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter  # estou settando um valor genérico para  ferramenta
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta


class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property  # por ser privado, é necessário usar o getter
    def marca(self):
        return self.__marca

    def escrever(self):  # metodo
        print("Caneta está escrevendo")


class MaquinaDeEscrever:

    def escrever(self):  # metodo
        print("Maquina está escrevendo")
