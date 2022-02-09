"""
Exercício Python 016:
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção
Inteira.
"""

''' from math import trunc
num = float(input('Digite um número: '))
nint = trunc(num)
print(f'O número {num} tem a parte inteira {nint}.') '''

from math import trunc
num = float(input('\33[33;1mDigite um número: '))
print(f'O número \33[1;34m{num}\33[33m tem a parte inteira \33[1;34m{trunc(num)}.')

'''from math import trunc
num = float(input('Digite um número: '))
print(f'O número {num} tem a parte inteira {num:.0f}.')'''