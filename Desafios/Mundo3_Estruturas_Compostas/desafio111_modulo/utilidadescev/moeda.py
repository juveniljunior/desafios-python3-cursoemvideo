def metade(num, formatacao=False):
    num = num / 2
    return num if formatacao is False else moeda(num)


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


def resumo(num, porcentaum, porcentdim):
    print(f'{"=+="*10}\n{"RESUMO DO VALOR":^30}\n{"=+="*10}')
    print(f'{"Preço analisado:":<20}{moeda(num)}'
          f'\n{"Dobro do preço:":<20}{dobro(num, True)}'
          f'\n{"Metade do Preço:":<20}{metade(num, True)}'
          f'\n{porcentaum:<3}{"% de aumento:":<17}{aumentar(num, porcentaum, True)}'
          f'\n{porcentdim:<3}{"% de redução:":<17}{diminuir(num, porcentdim, True)}'
          f'\n{"=+="*10}')
