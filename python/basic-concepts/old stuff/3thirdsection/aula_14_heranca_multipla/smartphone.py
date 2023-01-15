from eletronico import Eletronico
from log import LogMixin


# NESSA PARTE APRENDEMOS SOBRE HERANCA MISTA VEJA
class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):  # para conectar o telefone, ele precisa estar ligado
        if not self._ligado:
            error = f'{self._nome} não está ligado'
            print(error)
            self.log_error(error)
            return


        if self._conectado:
            error = f'{self._nome} Já está conectado'
            print(error)
            self.log_error(error)
            return

        self._conectado = True
        info = f'{self._nome} conectado com sucesso '
        self.log_info(info)

    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} já está desconectado '
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} desconectado com sucesso'
        print(info)
        self.log_info(info)
        self._conectado = False
