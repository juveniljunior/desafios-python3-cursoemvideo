"""
Exercício Python 075:
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""
numeros = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')),
           int(input('Digite só mais um número: ')),)
print(f'Os valores inseridos foram: {numeros}.\nO valor 9 apareceu {numeros.count(9)} vez(es).')
print(f'Os número(s) par(es) digitado(s) foram:', end=' ')
for p in numeros:
    if p % 2 == 0:
        print(f'{p}', end=' ')
print(f'\nO valor 3 foi digitado na {numeros.index(3)+1}ª posição.' if 3 in numeros
      else '\nO valor 3 não apareceu em nenhuma posição.')
