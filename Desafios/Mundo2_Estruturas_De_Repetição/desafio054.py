"""Exercício Python 054:
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas
pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""

from datetime import date
s = 0
s2 = 0
for c in range(1, 8):
    nascimento = int(input(f'Ano de nascimento da {c}º pessoa: '))
    if date.today().year - nascimento >= 21:
        s += 1
    else:
        s2 += 1
print(f'{s} pessoa(s) JÁ atingiram a maior idade!')
print(f' {s2} pessoa(S) NÃO são(ou é) maiores de idade!')
