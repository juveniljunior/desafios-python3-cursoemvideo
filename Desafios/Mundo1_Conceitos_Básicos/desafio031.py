"""Exercício Python 031:
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da
passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
"""

dis = float(input('Informe a distância da viagem (Km)? '))
if dis > 200.0:
    print(f'\033[1;31mVIAGEM LONGA!\033[m\n'
          f'\033[34mPREÇO DA PASSAGEM: \033[1;33m{dis*0.45:.2f}R$\033[m')
else:
    print(f'\033[1;35mVIAGEM ROZOÁVEL!\033[m\n'
          f'\033[34mPreço da passagem: \033[1;33m{dis*0.50:.2f}R$\033[m')
