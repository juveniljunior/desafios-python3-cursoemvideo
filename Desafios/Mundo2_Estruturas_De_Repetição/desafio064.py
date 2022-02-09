"""Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar
quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e
qual foi a soma entre eles (desconsiderando o flag).
"""

c = n = s = 0
while n != 999:
    n = int(input('Digite um número (ou 999 para parar): '))
    if n != 999:
        c += 1
        s += n
print(f'Foram digitados {c} números e a soma entre eles deu igual a {s}.')

"""c = n = s = 0
n = int(input('Digite um número (ou 999 para parar): '))
while n != 999:
    c += 1
    s += n
    n = int(input('Digite um número (ou 999 para parar): '))
print(f'Foram digitados {c} números e a soma entre eles deu igual a {s}.')"""
