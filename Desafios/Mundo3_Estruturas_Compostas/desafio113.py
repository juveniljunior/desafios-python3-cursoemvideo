"""
Exercício Python 113:
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da
digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""


def leiaInt(num):
    while True:
        try:
            num = int(input('Digite um Inteiro: '))
            break
        except (ValueError, TypeError):
            print('\33[31mERRO: Por favor, digite um número inteiro válido.\33[m')
    return num


def leiaFloat(num):
    while True:
        try:
            num = float(input('Digite um Real: '))
            break
        except (ValueError):
            print('\33[31mERRO! Por favor, digite um número real válido.\33[m')
    return num


nint = leiaInt('Digite um Nº Inteiro: ')
nreal = leiaFloat('Digite um Nº Real: ')
print(f'Você digitou o número inteiro {nint} e o número real {nreal}.')
