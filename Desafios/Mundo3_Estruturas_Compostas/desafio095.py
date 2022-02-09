"""
Exercício Python 095:
Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de
visualização de detalhes do aproveitamento de cada jogador.
"""

listatodososjog = list()
listadegols = list()

while True:
    totaldegols = 0
    fichajogador = {'nome': str(input(f'{"-"*45}\nNome do jogador: ')).title()}
    partidasjogadas = int(input(f'Quantas partidas {fichajogador["nome"]} jogou? '))
    for p in range(0, partidasjogadas):
        listadegols.append(int(input(f'Quantos gols na partida {p+1}? ')))
        totaldegols += listadegols[p]
    fichajogador['gols'] = listadegols[:]
    fichajogador['totaldegols'] = totaldegols
    listatodososjog.append(fichajogador)
    listadegols.clear()
    continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
    if continuar in 'Nn':
        break

print(f'{"=+="*20}\n{"COD":<5}{"NOME":<15}{"GOLS":<20}{"TOTAL":^5}\n{"-"*45}')
for pos, fichajogador in enumerate(listatodososjog):
    print(f'{pos:<5}{fichajogador["nome"]:<15}{str(fichajogador["gols"]):<20s}{fichajogador["totaldegols"]:^5}')
print(f'{"=+="*20}')
while True:
    p = int(input('Quer mostrar dados de qual jogador? [999 para parar] '))
    if p == 999:
        break
    elif p >= len(listatodososjog):
        print(f'ERRO! Não existe jogador com código {p}. Tente novamente!')
    for pos, fichajogador in enumerate(listatodososjog):
        if p == pos:
            print(f'---- LEVANTAMENTO DO JOGADOR {fichajogador["nome"].upper()} ----')
            for c, v in enumerate(fichajogador["gols"]):
                print(f'     No jogo {c+1} fez {v} gols.')
print('<<<< VOLTE SEMPRE >>>>')
