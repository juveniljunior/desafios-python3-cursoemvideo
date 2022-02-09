"""Exercício Python 027:
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o
último nome separadamente. """

nome = input('\033[37mDigite seu nome completo: ').strip()
nomed = nome.split()

print(f'\n\033[35mNOME COMPLETO: \33[33;1m{nome}\n'
      f'\n\033[35mPRIMEIRO: \33[33;1m{nomed[0]}\n'
      f'\033[35mÚLTIMO: \33[33;1m{nomed[-1]}')
