"""RACIOCÍNIO LOGÍCO"""
a = int(input('\033[34m1º VALOR: '))
b = int(input('\033[33m2º VALOR: '))
c = int(input('\033[32m3º VALOR: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(f'\033[33mO MENOR VALOR É \033[1;31m{menor}.\033[m')
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'\033[33mO MAIOR VALOR É \033[1;34m{maior}.')

"""LISTA TOTAL
valor = [int(input('1º VALOR: ')),
         int(input('2º VALOR: ')),
         int(input('3º VALOR: '))]
print(f'O MAIOR VALOR É {max(valor)}\n'
      f'O MENOR VALOR É {min(valor)}')"""

"""CONVERTE VARIAVEIS EM LISTA
a = int(input('1º VALOR: '))
b = int(input('2° VALOR: '))
c = int(input('3º VALOR: '))
abc = sorted([a, b, c])
print(f'O MENOR VALOR É {abc[0]}\n'
      f'O MAIOR VALOR É {abc[2]}')"""
