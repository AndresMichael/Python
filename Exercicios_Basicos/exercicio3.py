"""
Faça um programa que peça o primeiro nome do usuário . se o nome
tiver 4 letras ou menos escreva "seu nome é curto" , entre 5 e 7 letras , "nome normal ", maior que 7
"nome muito grande"
"""
nome = input('digite seu nome : ')
if len(nome) <= 4:
    print('seu nome é muito curto')
elif 4 < len(nome) <= 7:
    print('seu nome tem o tamanho normal ')
else:
    print('seu nome é muito grande')