# ANALISANDO TRIÂNGULOS 2.0
"""
Exercício Python 042:
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
"""

r1 = float(input('1º SEGUIMENTO: '))
r2 = float(input('2º SEGUIMENTO: '))
r3 = float(input('3º SEGUIMENTO: '))

if r2 + r3 > r1 and r1 + r3 > r2 and r1 + r2 > r3:
    print('É POSSÍVEL constrir um triângulo com essas medidas!')
    if r1 == r2 == r3:
        print('Este triângulo é classificado como EQUILÁTERO.')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('Este triângulo é classificado como ISOSCÉLES.')
    elif r1 != r2 != r3:
        print('Este triângulo é classificação como ESCALENO.')
else:
    print('NÃO É POSSÍVEL constrir um triângulo com essas medidas!')
