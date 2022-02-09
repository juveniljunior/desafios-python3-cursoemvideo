"""
Exercício Python 047:
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
"""

print('Os números pares de 1 a 50 são: ')
for c in range(1, 51, 2):
    print(f' {c+1},', end='')
print(end='.')
print('\nFIM')
