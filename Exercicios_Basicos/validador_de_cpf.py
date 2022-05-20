"""
CPF = 168.995.350-09
1 * 10 = 10              #  1 * 11 = 11
6 * 9 = 54               #  6 * 10 = 60
8 * 8 = 64               #  8 * 9 = 72
9 * 7 = 63               #  9 * 8 = 7
9 * 6 = 54               #  9 * 7 = 63
5 * 5 = 25               #  5 * 6 = 30
3 * 4 = 12               #  3 * 5 = 15
5 * 3 = 15               #  5 * 4 = 12
0 * 2 = 0                #  0 * 3 = 0
                         # digito1 * 2 = 0

----------------------------------------------
soma = 297                  soma = 343
11 - (297 % 11) = 11        11 - (343 % 11 ) = 9
11 > 9 = 0
digito1 = 0                 digito2 = 9
"""
entrada = input('digite seu CPF sem traços ou pontos, Apenas números : ')
CPF = entrada[0:9]
teste_cpf = []
new_cpf = []
soma = 0
soma2 = 0
for i in CPF:
    teste_cpf.append(int(i))

for i, cont_regresivo in enumerate(range(10, 1, -1)):
    valor = teste_cpf[i] * cont_regresivo
    soma += valor

conta = 11 - (soma % 11)

if conta > 9:
    digito1 = 0
else:
    digito1 = conta

teste_cpf.append(digito1)

for i, cont_regresivo in enumerate(range(11, 1, -1)):
    valor2 = teste_cpf[i] * cont_regresivo
    soma2 += valor2
conta2 = 11 - (soma2 % 11)
digito2 = conta2
teste_cpf.append(digito2)
print(teste_cpf)
for i in range(0, 11, 1):
    new_cpf.append(str(teste_cpf[i]))

novo_CPF = ''.join(new_cpf)
print(novo_CPF)
print(entrada)
sequencia = entrada == novo_CPF[0]*len(entrada)
if novo_CPF == entrada and not sequencia:
    print('Ótimo! Seu CPF é Válido ')
else:
    print('Seu CPF não é válido')