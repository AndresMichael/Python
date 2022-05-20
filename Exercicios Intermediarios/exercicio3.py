"""
3-Crie uma função que receba dois números . o primeiro é uma valor e o segundo é um percentual
exemplo (10%).retorne o primeiro numero somando o seu valor mais a porcentagem.
"""


def fx9(x, y):
    return x + (x * y / 100)


n1 = int(input('digite um número : '))
n2 = int(input('digite uma porcentagem :'))
conta = fx9(n1, n2)
print(conta)