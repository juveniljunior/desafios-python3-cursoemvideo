"""
Exercício Python 023:
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
"""

num = int(input('\33[37mDigite um número de 0 a 9999: '))

m = num // 1000 % 10
c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10

print(f'Analisando o \33[97;1m{num}...\n'
      f'\33[37mUNIDADE: \33[97;1m{u}\n'
      f'\33[37mDEZENA: \33[97;1m{d}\n'
      f'\33[37mCENTENA: \33[97;1m{c}\n'
      f'\33[37mMILHAR: \33[97;1m{m}')
