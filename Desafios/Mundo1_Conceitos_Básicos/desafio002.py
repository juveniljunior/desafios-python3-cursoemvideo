"""
Exercício Python 002:
Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
"""

dia = input('\33[36mQue dia você nasceu? ')
mes = input('Que mês você nasceu? ')
ano = input('Que ano você nasceu? \33[m')

print('\33[33mVocê nasceu no dia\33[1;36m', dia, '\33[33mde\33[1;36m', mes, '\33[33mde\33[1;36m', ano)
