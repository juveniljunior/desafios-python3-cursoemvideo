"""
Exercício Python 009:
Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
"""

num = int(input('\33[37mDigite um número para ver a sua tabuada: \33[m'))
contador = 0

print(12*"\33[33m-")

while contador < 10:
    contador += 1
    res = num * contador
    print(f'\33[1;31m{num} x \33[1;34m{contador:2} = \33[1;97m{res}')

print(12*'\33[33m-')
