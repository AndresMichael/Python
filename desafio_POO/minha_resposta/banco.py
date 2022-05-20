class Banco:
    def __init__(self):
        self.agencia = [111, 222, 333]
        self.cliente = []
        self.conta = []

    def add_conta(self, conta):
        self.conta.append(conta)

    def add_cliente(self, cliente):
        self.cliente.append(cliente)

    def autentica(self, cliente):
        if cliente not in self.cliente:
            return False
        if cliente.conta not in self.conta:
            return False
        if cliente.conta.agencia not in self.agencia:
            return False

        return True