"""
Exercício Python 096:
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
retangular (largura e comprimento) e mostre a área do terreno.
"""


def calcArea(l, c):
    a = l * c
    print(f'A aréa de um terreno de {l:.1f} X {c:.1f} é de {a:.1f} m².')


# PROGRAMA PRINCIPAL
print(f'CONTROLE DE TERRENOS\n{"-" * 20}')
calcArea(float(input('LARGURA (m): ')), float(input('CUMPRIMENTO (m): ')))
