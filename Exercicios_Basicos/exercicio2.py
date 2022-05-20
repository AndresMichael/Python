"""
Faça um programa que pergunte a hora para o usuário , e baseado no horário descrito exiba a
saudação adequada

"""

hora = input('digite a hora  sem os minutos ')

if hora.isdigit():
    hora = int(hora)
    if hora < 0 or hora > 23:
        print('valor invalido')
    elif 0 < hora <= 12:
        print('bom dia')
    elif 12 < hora <= 18:
        print('boa tarde ')
    elif 18 < hora <= 23:
        print('bom dia')
else:
    print('por favor digite um valor corretog')