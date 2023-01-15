import re

class Calcipv4:
    def __init__(self, ip, mascara=None, prefixo=None):
        self.ip = ip
        self.mascara = mascara
        self.prefixo = prefixo

        self._set_broadcast()

    @property
    def ip(selfs):
        return self._ip

    @property
    def mascara(self):
        return self._mascara

    @property
    def prefixo(self):
        return self._prefixo

    @ip.setter
    def ip(self, valor):
        if not self._valida_ip(valor):

            raise ValueError('Ip invalido')

        self._ip = valor
        self.ip_bin = self._ip_to_bin(valor)

    @mascara.setter
    def mascara(self, valor):
        if not valor:
            return

        if not self._valida_ip(valor):
            raise ValueError('Mascara inválida')

        self._mascara = valor
        self._mascara_bin = self._ip_to_bin(valor)

        if not hasattr(self, 'prefixo'):
            self.prefixo = self._mascara_bin.count('1')

    @prefixo.setter
    def prefixo(self, valor):
        if not valor:
            return

        if not isinstance(valor, int):
            raise TypeError('tipo invalido, necessita de inteiro')

        if valor > 32:
            raise ValueError('o prefixo precisa ter 32 bits ')

        self._prefixo = valor
        self._mascara_bin = (valor * '1').ljust(32, '0')

        if not hasattr(self, mascara):
            self.mascara = self._bin_to_ip(self._mascara_bin)

    @staticmethod
    def _valida_ip(ip):
        regexp = re.compile(
            r'^([0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3})$'
        )

        if regexp.search(ip):
            return True

    @staticmethod
    def _ip_to_bin(ip):
        blocos = ip.split('.')
        blocos_binario = [bin(int(x))[2:].zfill(8) for x in blocos]
        return ''.join(blocos_binario)

    @staticmethod
    def _bin_to_ip(ip):
        n = 8
        blocos = [str(int(ip[i:n+i], 2)) for i in range(0,32,n)]
        return '.'.join(blocos)

    def _set_broadcast(self):
        host_bits = 32 - self.prefixo
        return  self._ip_bin[0:self.prefixo] + (host_bits * '1')
