"""
Exercício Python 103:
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
mesmo que algum dado não tenha sido informado corretamente.
"""


def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador \33[32;1m{nome}\33[m fez \33[33;1m{gols}\33[m gols no campeonato.')


# PROGRAMA PRINCIPAL
print('\33[1;37m=\33[m' * 45)
n = str(input('Nome do jogador: ')).title()
g = str(input('Número de gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == "":
    ficha(gols=g)
else:
    ficha(n, g)
