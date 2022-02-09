"""
Exercício Python 099:
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com
valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""


def maior(* listnumeros):
    mai = c = 0
    print("\33[1;37m-=\33[m" * 30)
    print(f'Analisando os valores passados...')
    for num in listnumeros:
        print(f'\33[97;1m{num} \33[m', end='')
        if c == 0:
            mai = num
        else:
            if num > mai:
                mai = num
        c += 1
    print(f'Foram informados \33[97;1m{len(listnumeros)}\33[m números ao todo.')
    print(f'O maior valor informado foi \33[97;1m{mai}\33[m.')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(6)
maior()
