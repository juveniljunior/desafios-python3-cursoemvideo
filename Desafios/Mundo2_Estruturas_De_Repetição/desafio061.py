# PROGRESSÃO ARITMÉTICA v2.0
"""
Exercício Python 061:
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
da progressão usando a estrutura while.
"""

contador = 0
primeirotermo = int(input('1º TERMO DA PA: '))
razao = int(input('RAZÃO DA PA: '))
novocontador = 1
print(f'{primeirotermo},', end='')
while contador < 9:
    primeirotermo += razao
    contador += 1
    print(f'{primeirotermo},' if contador < 9 else f'{primeirotermo}...', end='')
