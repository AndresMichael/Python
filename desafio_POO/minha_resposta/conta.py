from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor

    def extrato(self):
        print(f'Agencia: {self.agencia}\nConta:{self.conta}\nSaldo: {self.saldo}')

    def deposito(self, valor):
        if not isinstance(valor, (int, float)):
            print('Erro : Valor não aceito')
            return
        self.saldo += valor

    @abstractmethod
    def sacar(self, valor):
        pass


class CB(Conta):
    def __init__(self, agencia, conta, saldo):
        super().__init__(agencia, conta, saldo)

    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            print('Erro : Valor não aceito')
            return
        if valor > self.saldo:
            print(f'o valor solicitado é maior que seu saldo:{self.saldo}')
            return
        self.saldo -= valor


class CC(Conta):
    def __init__(self, agencia, conta, saldo, limite=50):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            print('Erro : Valor não aceito')
            return
        if valor > (self.saldo + self.limite):
            print(f'o valor solicitado é maior que seu saldo:R$ {self.saldo} e o limite permitido de R$ {self.limite}')
            return
        self.saldo -= valor
