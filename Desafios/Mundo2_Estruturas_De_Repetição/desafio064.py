# TRATANDO VÁRIOS VALORES
c = n = s = 0
while n != 999:
    n = int(input('Digite um número (ou 999 para parar): '))
    if n != 999:
        c += 1
        s += n
print(f'Foram digitados {c} números e a soma entre eles deu igual a {s}.')

"""c = n = s = 0
n = int(input('Digite um número (ou 999 para parar): '))
while n != 999:
    c += 1
    s += n
    n = int(input('Digite um número (ou 999 para parar): '))
print(f'Foram digitados {c} números e a soma entre eles deu igual a {s}.')"""
