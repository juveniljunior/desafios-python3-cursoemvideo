# CÁLCULO DO FATORIAL
"""from time import sleep
n = int(input('Digite um número e veja seu fatorial: '))
res = n
contador = n
print(f'{n}! = {n} X ', end='')
while contador >= 2:
    contador -= 1
    res *= contador
    sleep(0.22)
    print(f'{contador} X ' if contador > 1 else f'{contador} = ', end='')
print(res)"""

n = int(input('Digite um número e veja seu fatorial: '))
c = n + 1
f = 1
print(f'CALCULANDO {n}! = {n} X ', end='')
for c in range(1, n):
    c += 1
    n -= 1
    f *= c
    print(f'{n} X ' if n > 1 else f'{n} = ', end='')
print(f)
