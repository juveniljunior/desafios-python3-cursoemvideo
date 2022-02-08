"""
Exercício Python 097:
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como
parâmetro e mostre uma mensagem com tamanho adaptável.
"""


def escreva(txt):
    print("-" * (len(txt)+4))
    print(txt.center(len(txt)+4))
    print("-" * (len(txt)+4))


# PROGRAMA PRINCIPAL
escreva('JUVENIL JUNIOR')
escreva('18 YEARS')
escreva('FUTURE PROGRAMMER')
escreva('SEVENTH DAY ADVENTIST')
