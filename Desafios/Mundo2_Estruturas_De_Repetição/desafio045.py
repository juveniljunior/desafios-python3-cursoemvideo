# PEDRA, PAPEL E TESOURA
"""
Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
"""

from random import choices
from time import sleep
comp = choices(['PEDRA', 'PAPEL', 'TESOURA'])
print('-=-'*10)
print(f'{" JOGO DO JOQUEMPÔ ":=^30}')
print('-=-'*10)
print('Tente ganhar de mim!')
usu = str(input('PEDRA-PAPEL-TESOURA!\nQual sua jogada? ')).strip().upper().split()
print('PROCESSANDO...')
sleep(2)
print('PEDRA')
sleep(0.5)
print('PAPEL')
sleep(1)
print('TESOURA!')
if comp == usu:
    print('EMPATE! Jogue novamente!')
elif usu == ['TESOURA'] or usu == ['PEDRA'] or usu == ['PAPEL']:
    if comp == ['PEDRA'] and usu == ['TESOURA'] or comp == ['TESOURA'] and usu == ['PAPEL'] or comp == [
        'PAPEL'] and usu == ['PEDRA']:
        print(f'EU GANHEI! Você escolheu {usu} e eu {comp} e {comp} ganha {usu}!')
    else:
        print(f'PARABÉNS! VOCÊ ME VENCEU! pois escolheu {usu} e eu {comp} e {usu} ganha {comp}!')
else:
    print('Você digitou um valor inválido!')
