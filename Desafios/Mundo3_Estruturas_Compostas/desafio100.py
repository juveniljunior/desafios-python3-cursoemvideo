"""
Exercício Python 100:
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e
somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a
soma entre todos os valores pares sorteados pela função anterior.
"""


def sorteia(lista):
    from random import randint
    from time import sleep
    pos = 0
    print(f'Sortenado 5 valores da lista: ', end='')
    while pos < 5:
        lista.append(randint(1, 10))
        print(f'\33[32;1m{lista[pos]}\33[m ', end='')
        sleep(0.8)
        pos += 1
    print('| PRONTO!')


def somaPar(lista):
    from time import sleep
    sp = 0
    print(f'Somando os valores pares da lista que são ', end='')
    for num in lista:
        if num % 2 == 0:
            print(f'\33[33;1m{num}\33[m ', end='')
            sleep(0.6)
            sp += num
    print(f'temos \33[34;1m{sp}\33[m')


numeros = []
sorteia(numeros)
somaPar(numeros)
