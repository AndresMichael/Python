"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra. Banco
tem clientes e contas.

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
"""
from banco import Banco
from conta import CB, CC
from cliente import Cliente
banco = Banco()

c1 = Cliente('Michael', 21)
c2 = Cliente('Layane', 22)
c3 = Cliente('Emili', 21)

conta1 = CB(222, 2222, 750)
conta2 = CC(333, 2222, 350, limite=200)
conta3 = CB(111, 4321, 0)

c1.inserir_conta(conta1)
c2.inserir_conta(conta2)
c3.inserir_conta(conta3)

banco.add_cliente(c1)
banco.add_conta(conta1)

banco.add_cliente(c2)
banco.add_conta(conta2)

banco.add_cliente(c3)
banco.add_conta(conta3)

if banco.autentica(c1):
    conta1.deposito(100)
    print(f'Cliente: {c1.nome}')
    conta1.extrato()
else:
    print('Cliente não autenticado.')
print('======================================================')

if banco.autentica(c2):
    print(f'Cliente: {c2.nome}')
    conta2.extrato()
else:
    print('Cliente não autenticado.')
print('======================================================')

if banco.autentica(c3):
    print(f'Cliente: {c3.nome}')
    conta3.deposito(1000)
    conta3.sacar(1500)
else:
    print('Cliente não autenticado.')

