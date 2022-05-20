"""
crie uma função f1 que recebe uma função f2 como parâmetro e retorne o valor de f2 executada
"""


def media(*args):
    cont = 0
    tamanho = len(args)
    for i in range(tamanho):
        cont = cont + args[i]
    return cont / tamanho


def mestre(function, *args, **kwargs):
    return function(*args, **kwargs)


teste3 = mestre(media, 25, 15, 5, 40, 15)
print(teste3)


def hello(nome):
    return f'oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} caro Sr. {nome}'


teste1 = mestre(hello, 'micha')
teste2 = mestre(saudacao, 'katia', 'ola')
print(teste1)
print(teste2)
