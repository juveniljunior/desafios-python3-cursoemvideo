"""
Exercício Python 074:
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
números gerados e também indique o menor e o maior valor que estão na tupla.

"""
from random import randint
numerossorteados = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram:', end=' ')
for c in range(0, len(numerossorteados)):
    print(f'{numerossorteados[c]}', end=' ')
print(f'\nOs maior valor sorteado foi {max(numerossorteados)}.\nO menor valor sorteado foi {min(numerossorteados)}.')
