def metade(num):
    return num / 2


def dobro(num):
    return num * 2


def aumentar(num, porcentagem):
    num = num + (num * (porcentagem / 100))
    return num


def diminuir(num, porcentagem):
    num = num - (num * (porcentagem / 100))
    return num