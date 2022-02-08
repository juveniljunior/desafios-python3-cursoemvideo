"""
Exercício Python 091:
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde
esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado.

SOLUÇÃO UTLIZANDO O MÓDULO OPERATOR(ITEMGETTER)"""

from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}
ranking = list()
print(f'{"VALORES SORTEADOS":^30}\n{"=+="*10}')
for k, v in jogo.items():
    print(f'   {k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(f'{"=+="*10}\n{"RANKING DOS JOGADORES":^30}\n{"=+="*10}')
for pos, v in enumerate(ranking):
    print(f'   {pos+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)

"""MINHA SOLUÇÃO UTILIZANDO O RACIOCÍNIO LÓGICO
from random import randint
from time import sleep
c = 1
nc = maiordasobra = menordasobra = 0
jogadores = {'Jogador1': randint(1, 6), 'Jogador2': randint(1, 6), 'Jogador3': randint(1, 6), 'Jogador4': randint(1, 6)}
print(f'{"VALORES SORTEADOS":^30}\n{"=+="*10}')
for k, v in jogadores.items():
    print(f'   {k} tirou {v} no dado.')
    sleep(0.7)
menor = min(jogadores.values())
maior = max(jogadores.values())
print(f'{"=+="*10}\n{"RANKING DOS JOGADORES":^30}\n{"=+="*10}')
for key, valor in jogadores.items():
    if valor == maior:
        print(f'   {c}º lugar: {key} com {valor}.')
        sleep(0.7)
        c += 1
    if c == 4:
        break
for key, valor in jogadores.items():
    if maior > valor > menor:
        if nc == 0:
            maiordasobra = menordasobra = valor
            nc += 1
        else:
            if valor > maiordasobra:
                maiordasobra = valor
            if valor < menordasobra:
                menordasobra = valor
for key, valor in jogadores.items():
    if valor == maiordasobra:
        print(f'   {c}º lugar: {key} com {valor}.')
        sleep(0.7)
        c += 1
if maiordasobra == menordasobra:
    del menordasobra
else:
    for key, valor in jogadores.items():
        if valor == menordasobra:
            print(f'   {c}º lugar: {key} com {valor}.')
            sleep(0.7)
            c += 1
for key, valor in jogadores.items():
    if valor == min(jogadores.values()):
        print(f'   {c}º lugar: {key} com {valor}.')
        sleep(0.7)
        c += 1
"""
