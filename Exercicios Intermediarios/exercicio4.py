"""
4-Fizz Buzz - Se o parâmetro da função for divisível por 2 , retorne fizz
se for divisível or 5 retorne Buzz. Se o parâmetro for divisível por 3 e 5
retorne FizzBuzz.Caso contrário retorne o número
"""


def function(x):
    if x % 2 == 0:
        return f"{x} é divisível por 2 Fizz"
    elif x % 5 == 0 and x % 3 == 0:
        return f"{x} é divisível por 3 e 5 FizBuzz"
    elif x % 5 == 0:
        return f"{x} é divisível por 5 Buzz"
    else:
        return x


# n1 = int(input('digite um número :'))
# retorno = function(n1)
# print(retorno)
from random import randint

for i in range(100):
    aleatorio = randint(0, 100)
    print(function(aleatorio))
