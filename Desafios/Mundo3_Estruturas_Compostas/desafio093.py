"""
Exercício Python 093:
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler
o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final,
tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""

aprovjog = {'nome': str(input('Nome do jogador: ')).title()}
totalp = int(input(f'Quantas partidas {aprovjog["nome"]} jogou? '))
golsporpart = list()
totalgols = 0
for p in range(0, totalp):
    golsporpart.append(int(input(f'    Quantos gols pa partida {p}? ')))
    totalgols += golsporpart[p]
aprovjog['gols'] = golsporpart
aprovjog['total'] = totalgols
print(f'{"=+="*20}')
print(f'{aprovjog}')
print(f'{"=+="*20}')
for k, v in aprovjog.items():
    print(f'O {k} tem o valor de {v}')
print(f'{"=+="*20}')
print(f'O jogador {aprovjog["nome"]} jogou {totalp} partidas.')
for p, v in enumerate(aprovjog['gols']):
    print(f'    ➠ Na partida {p}, fez {aprovjog["gols"][p]} gols.')
print(f'Foi um total de {totalgols} gols.')
