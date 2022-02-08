"""cont = 1
while cont <= 10:
    print(cont, end=' ')
    cont += 1
print('ACABOU')"""
s = c = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'Foram digitados {c} números e a soma entre os números foi igual a {s}.')
