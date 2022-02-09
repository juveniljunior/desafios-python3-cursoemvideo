"""
Exercício Python 106:
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o
comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use
cores.
"""

from time import sleep


def escreva(text):
    tam = len(text)
    print('\33[7;49;34m=' * (tam + 4))
    print(text.center(tam + 4))
    print('=' * (tam + 4))
    print('\33[m', end='')
    sleep(1)


def sistajuda(funbib):
    escreva(f'Acessando manual do comando "{funbib}"')
    print('\33[7;49;97m')
    help(funbib)
    print('\33[7;49;97m')
    sleep(1)


# PROGRAMA PRINCIPAL
while True:
    print(f'\33[7;49;32m{"=" * 30}\n{"SISTEMA DE AJUDA PyHELP":^30}\n{"=" * 30}')
    funcmet = input('\33[mFunção ou Blibioteca > ').lower().strip()
    if funcmet == 'fim':
        break
    else:
        sistajuda(funcmet)
print('\33[36;1m\nATÉ LOGO!')

