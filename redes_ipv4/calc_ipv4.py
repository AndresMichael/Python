import re


class CalcIPV4:
    def __init__(self, ip, mask=None, cidr=None):
        self.ip = ip
        self.mask = mask
        self.cidr = cidr
        if mask is None and cidr is None:
            raise ValueError('ERRO: precisa envir máscara ou cidr, não ambos.')

        if mask and cidr:
            raise ValueError('ERRO:  não pode enviar ambos.')
        self._set_broadcast()
        self._set_rede()

    @property
    def rede(self):
        return self._rede

    @property
    def broadcast(self):
        return self._broadcast

    @property
    def ips_validos(self):
        return self.n_ips_validos()

    @property
    def ip(self):
        return self._ip

    @property
    def mask(self):
        return self._mask

    @property
    def cidr(self):
        if self._cidr is None:
            return

        return self._cidr

    @ip.setter
    def ip(self, ip):
        if not self.autentica_ip(ip):
            raise ValueError('ERRO: endereço de ip inválido')
        self._ip = ip
        self._ip_bin = self.ip_para_binario(ip)

    @mask.setter
    def mask(self, mask):
        if not mask:
            return

        if not self.autentica_ip(mask):
            raise ValueError('ERRO: endereço de máscara inválido')

        self._mask = mask
        self._mask_bin = self.ip_para_binario(mask)

        if not hasattr(self, 'cidr'):
            self.cidr = self._mask_bin.count('1')

    @cidr.setter
    def cidr(self, cidr):
        if not cidr:
            return

        if not isinstance(cidr, int):
            raise TypeError('ERRO: tipo não suportado')

        if cidr > 32 or cidr < 0:
            raise ValueError('ERRO: valor não permitido')

        self._cidr = cidr
        self._mask_bin = (cidr * '1').ljust(32, '0')

        if not hasattr(self, 'mask'):
            self.mask = self.binario_para_ip(self._mask_bin)

    @staticmethod
    def autentica_ip(ip):
        regex = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$'
        )
        if regex.search(ip):
            return True
        else:
            return False

    @staticmethod
    def ip_para_binario(ip):
        blocos = ip.split('.')
        blocos_bin = [bin(int(x))[2:].zfill(8) for x in blocos]
        return ''.join(blocos_bin)

    @staticmethod
    def binario_para_ip(ip):
        n = 8
        blocos = [str(int(ip[x:x + n], 2)) for x in range(0, 32, n)]
        return '.'.join(blocos)

    def _set_broadcast(self):
        hosts = 32 - self.cidr
        self._broadcast_bin = self._ip_bin[:self.cidr] + (hosts * '1')
        self._broadcast = self.binario_para_ip(self._broadcast_bin)
        return self._broadcast

    def _set_rede(self):
        host = 32-self.cidr
        self._rede_bin = self._ip_bin[:self.cidr] + (host*'0')
        self._rede = self.binario_para_ip(self._rede_bin)
        return self._rede

    def n_ips_validos(self):
        return 2 ** (32 - self.cidr)
