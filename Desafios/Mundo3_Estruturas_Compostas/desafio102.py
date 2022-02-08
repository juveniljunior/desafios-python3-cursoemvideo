"""
Exercício Python 102:
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que
indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não
na tela o processo de cálculo do fatorial.
"""


def fatorial(num, show=False):
    """
    => Esta função mostra o valor fatorial de um número inserido no 1º parâmetro.
    :param num: Recebe o número a ser calculado o resulatado so seu fatorial
    :param show: (Opcional) Mostra a sequência de números multiplicados para se chegar ao valor fatorial do número.
    :return: retorna o valor do fatorial do número.
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            if c > 1:
                print(f'{c} X ', end='')
            if c == 1:
                print(f'{c} = {f}')
    if not show:
        print(f)
    return f


# PROGRAMA PRINCIPAL
fatorial(6, True)
#  help(fatorial)
