def metade(num=0):
    num = num / 2
    return num


def dobro(num=0):
    num = num * 2
    return num


def aumentar(num=0, porcentagem=0):
    num = num + (num * (porcentagem / 100))
    return num


def diminuir(num=0, porcentagem=0):
    num = num - (num * (porcentagem / 100))
    return num


def moeda(num, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')

