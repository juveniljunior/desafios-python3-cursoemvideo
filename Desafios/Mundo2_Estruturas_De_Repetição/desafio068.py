# JOGO DO ÍMPAR OU PAR
"""
Exercício Python 068:
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando
o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""

from random import randint
vitorias = 0
print(f'{"="*40:^40}\n{" VAMOS JOGAR PAR OU ÍMPAR ":-^40}\n{"="*40}')
while True:
    computador = randint(1, 100)
    numerodojogador = int(input('Diga um valor: '))
    opcaodojogador = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    soma = numerodojogador + computador
    resutado = soma % 2
    print(f'Você jogou {numerodojogador} e o computador {computador}.\nTotal de {soma} é ', end='')
    if resutado == 0:  # se  o resultado for PAR
        print(f'PAR!')
        if opcaodojogador == 'I':
            print('VOCÊ PERDEU!')
            break
        else:
            print('VOCÊ GANHOU!')
            vitorias += 1
    elif resutado != 0:  # se  o resultado for IMPAR
        print('ÍMPAR!')
        if opcaodojogador == 'P':
            print(f'VOCÊ PERDEU!\n{"="*40}')
            break
        else:
            print(f'VOCÊ GANHOU!\n{"="*40}')
            vitorias += 1
print(f'GAME OVER! Você venceu {vitorias} vez(es)!')
