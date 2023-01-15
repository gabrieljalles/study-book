#uma classe será dona dos objetos de outra classe

class Cliente:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = [] # um cliente pode ter vários enderecos, nesse caso, é uma boa prática criar a própria classe endereco

    def inserir_endereco(self,cidade,estado):
        self.enderecos.append(Endereco(cidade,estado))

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self): # USADO SOMENTE PARA MOSTRAR QUE O OBJETO FOI APAGADO, ELE NÃO APAGA NADA
        print(f'{self.nome} FOI APAGADO')

# Dessa forma, a classe Endereco pertence a classe Cliente, se apagar a  Cliente a endereco vai junto. veja  o del na outra pagina
class Endereco:
    def __init__(self,cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.cidade}/{self.estado} foi apagado')