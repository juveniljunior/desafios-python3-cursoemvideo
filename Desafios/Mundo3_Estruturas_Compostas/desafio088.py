"""
Exercício Python 088:
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar
quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""

from time import sleep
from random import randint
jogos = list()
jogo = list()
contjogos = 1
print(f'{"=+="*15}\n{"JOGO DA MEGA SENA":^45}\n{"=+="*15}')
njogopedido = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'{"+="*5} SORTEANDO {njogopedido} JOGOS {"+="*5}')
while contjogos <= njogopedido:
    contnum = 0
    while contnum < 6:
        n = randint(1, 60)
        if n not in jogo:
            jogo.append(n)
            contnum += 1
        if contnum == 6:
            jogo.sort()
            jogos.append(jogo[:])
            jogo.clear()
    contjogos += 1
for c, jogo in enumerate(jogos):
    print(f'Jogo {c+1}: {jogo}')
    sleep(1)
print(f'{" < BOA SORTE > ":=^20}')
