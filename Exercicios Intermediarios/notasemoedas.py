"""
Leia um valor de ponto flutuante com duas casas decimais.
 Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas
 possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2.
 As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.
"""
nota100 = nota50 = nota20 = nota10 = nota5 = nota2 = 0
moeda1 = moeda05 = moeda025 = moeda010 = moeda005 = moeda001 = 0
lista = input().split('.')
dinheiro = int(lista[0])
moeda = int(lista[1])/100

while dinheiro >= 100:
    nota100 += 1
    dinheiro -= 100

while dinheiro >= 50:
    nota50 += 1
    dinheiro -= 50

while 20 <= dinheiro < 50:
    nota20 += 1
    dinheiro -= 20

while 10 <= dinheiro < 20:
    nota10 += 1
    dinheiro -= 10

while 5 <= dinheiro < 10:
    nota5 += 1
    dinheiro -= 5
while 2 <= dinheiro < 5:
    nota2 += 1
    dinheiro -= 2

moeda += dinheiro

while moeda >= 1:
    moeda1 += 1
    moeda -= 1

while moeda >= 0.5:
    moeda05 += 1
    moeda = moeda - 0.5

while moeda >= 0.25:
    moeda025 += 1
    moeda -= 0.25

while moeda >= 0.10:
    moeda010 += 1
    moeda -= 0.10

while moeda >= 0.05:
    moeda005 += 1
    moeda -= 0.05

while round(moeda, 2) >= 0.01:
    moeda001 += 1
    moeda -= 0.01

print(f'NOTAS:'
      f'\n{nota100} nota(s) de R$ 100.00'
      f'\n{nota50} nota(s) de R$ 50.00'
      f'\n{nota20} nota(s) de R$ 20.00'
      f'\n{nota10} nota(s) de R$ 10.00'
      f'\n{nota5} nota(s) de R$ 5.00'
      f'\n{nota2} nota(s) de R$ 2.00')
print(f'Moedas:'
      f'\n{moeda1} nota(s) de R$ 1.00'
      f'\n{moeda05} nota(s) de R$ 0.50'
      f'\n{moeda025} nota(s) de R$ 0.25'
      f'\n{moeda010} nota(s) de R$ 0.10'
      f'\n{moeda005} nota(s) de R$ 0.05'
      f'\n{moeda001} nota(s) de R$ 0.01')







