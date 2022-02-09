"""
Exercício Python 049:
Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora
utilizando um laço for.
"""

n = int(input('Digite um número para ver sua tabuada: '))
print('='*12)
for c in range(1,11):
    print(f'{n} X {c} = {n*c}')
print('='*12)
