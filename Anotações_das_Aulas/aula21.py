"""help(sorted)
print(sorted.__doc__)


def contador(i, f, p):
    '''=> Faz uma contagem e mostra na tela
    :param i: Início da contagem
    :param f: Final do contagem
    :param p: Passo da contagem
    :return: Sem retorno
    '''
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM')


help(contador)


def somar(a=0, b=0, c=0, d=0):
    s = a + b + c + d
    print(f'A soma vale {s}.')


somar(35, 15, 10, 15)


def teste(b):
    global a
    a = 8
    b += 5
    c = 2
    print(f'  A dentro vale {a}')
    print(f'  B dentro vale {b}')
    print(f'  C dentro vale {c}')


a = 10
teste(a)
print(f'A fora vale {a}')


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(5, 2, 3)
r2 = somar(9, 7)
r3 = somar(7)
print(f'Os resultados da soma são {r1}, {r2} e {r3}.')


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f' Os resultaodos dos fatoriais são {f1}, {f2} e {f3}.')"""


def par(num):
    if num % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É PAR!')
else:
    print('É ÍMPAR!')
