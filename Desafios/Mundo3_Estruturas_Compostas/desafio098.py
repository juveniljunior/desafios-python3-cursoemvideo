"""Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""


def contador(inicio, fim, passo):
    from time import sleep
    if passo < 0:
        passo *= -1
    elif passo == 0:
        passo = 1
    print("\33[1m-=\33[m" * 30)
    print(f'Contando de {inicio} até {fim} de {passo} em {passo}')
    sleep(1.2)
    c = inicio

    if inicio < fim:
        for num in range(inicio, fim+1, passo):
            print(f'{num} ', end='')
            sleep(0.3)
        print('| FIM')
    elif inicio > fim:
        while fim <= inicio:
            print(f'{c} ', end='')
            sleep(0.3)
            fim += passo
            c -= passo
        print('| FIM')


# PROGRAMA PRINCIPAL
contador(1, 10, 1)
contador(10, 0,  2)
print("\33[1m-=\33[m"*30)
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
