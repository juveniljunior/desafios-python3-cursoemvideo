"""
Exercício Python 050:
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem
pares. Se o valor digitado for ímpar, desconsidere-o.
"""

s = 0
cont = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        s += n
        cont += 1
print(f'Você digitou {cont} números PARES e a soma entre eles foi igual a {s}.')
