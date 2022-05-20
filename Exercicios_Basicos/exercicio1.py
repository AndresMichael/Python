"""
faça um programa que peça para o usuário digitar um numero inteiro,
informar se este número é par ou ímpar. Caso o usuário não digite um número inteiro
informe que não é numero inteiro.
"""
numero_int = input('digite um número inteiro : ')
# a função isnumeric() é utilizada para saber se o numero é inteiro e retorna um valor boolean
if numero_int.isnumeric():  # aqui já afirma que o numero é inteiro ou seja que é True

    print('numero digitado é inteiro ')
    if int(numero_int) % 2 == 0:
        print('o número digitado é par ')
    else:
        print('o numero digitado é impar ')

else:
    print('o número digitado não é inteiro tente novamente ')
