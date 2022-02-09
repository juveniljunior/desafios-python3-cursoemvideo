"""
Exercício Python 032:
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""

from datetime import date
ano = int(input('\033[37mQue ano você quer analisar? Digite 0 para analisar o ano atual: \033[m'))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 or ano % 400 == 0) and ano % 100 != 0:
    print(f'\033[35mO ano de \033[1;37;4m{ano}\033[m\033[35m é BISSEXTO!\033[m')
else:
    print(f'\033[31mO ano de \033[1;4;37m{ano}\033[m \033[31mNÃO é um ano BISSEXTO!\033[m')

"""OPÇÃO COM O MODULO CALENDAR
from datetime import date
from calendar import isleap
ano = int(input('\033[37mQue ano você quer analisar? Digite 0 para analisar o ano atual: \033[m'))
if ano == 0:
    ano = date.today().year
if isleap(ano):
    print(f'\033[35mO ano de \033[1;37;4m{ano}\033[m\033[35m é BISSEXTO!\033[m')
else:
    print(f'\033[31mO ano de \033[1;4;37m{ano}\033[m \033[31mNÃO é um ano BISSEXTO!\033[m')"""
