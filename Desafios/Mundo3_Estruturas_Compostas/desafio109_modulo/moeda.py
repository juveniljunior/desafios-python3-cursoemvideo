def metade(res, formatacao=False):
    res = res / 2
    return res if formatacao is False else moeda(res)


def dobro(num, formatacao=False):
    num = num * 2
    return num if formatacao is False else moeda(num)


def aumentar(num, porcentagem, formatacao=False):
    num = num + (num * (porcentagem / 100))
    return num if formatacao is False else moeda(num)


def diminuir(num, porcentagem, formatacao=False):
    num = num - (num * (porcentagem / 100))

    return num if formatacao is False else moeda(num)


def moeda(num):
    return f'R${num:.2f}'.replace('.', ',')
