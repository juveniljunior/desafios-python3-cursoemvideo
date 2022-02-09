"""
Exercício Python 082:
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas
extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
"""

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
