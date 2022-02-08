# DIVIDINDO VALORES EM UMA LISTA
numeros = numerospares = numerosimpares = []
while True:
    numeros.append(int(input('Digite um número: ')))
    resposta = ''
    while resposta != 'S' and resposta != 'N':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
for n in numeros:
    if n % 2 == 0:
        numerospares.append(n)
    else:
        numerosimpares.append(n)
print(f'{"-="*30}\nA lista completa é {numeros}\nA lista de pares é {numerospares}\nA lista dos ímpares é {numerosimpares}')
