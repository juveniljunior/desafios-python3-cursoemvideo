"""
Exercício Python 052:
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""

'''n = int(input('Digite um número inteiro: '))

if n % 1 == 0 and n % n == 0 and n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 11 != 0:
    print(f'{n} é um número PRIMO!')
else:
    print(f'{n} NÃO é um número primo!')'''
n = int(input('Digite um número inteiro: '))
cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        cont += 1
        print(f'\33[33;1m{c}', end=' ')
    else:
        print(f'\33[31;1m{c}\33[m', end=' ')
if cont <= 2:
    print(f'\33[34;m\n{n} É um número PRIMO!\nPois foi divisível apenas {cont} vezes!')
elif cont > 2:
    print(f'\33[37;m\n{n} NÃO é um número PRIMO! \nPois foi divisível {cont} vezes!')
else:
    print('Número inválido!')
