"""def soma(a, b):
    print(f'A = {a} | B = {b}')
    s = a + b
    print(f'A SOMA A + B = {s}')


# PROGRAMA PRINCIPAL
soma(b=4, a=5)
soma(8, 9)
soma(2, 3)


def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM')
"""


def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')


contador(1, 3, 5, 7)
contador(2, 4, 6)
contador(10, 20, 30, 40, 50, 60)
