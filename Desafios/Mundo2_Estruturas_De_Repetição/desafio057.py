"""Exercício Python 057:
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso
esteja errado, peça a digitação novamente até ter um valor correto.
"""

sexo = str(input('Qual seu sexo? M ou F? ')).upper().strip()[0]
while sexo not in 'FM':
    sexo = str(input('Dados inválidos! Qual seu sexo? M ou F? ')).upper().strip()[0]
print(f'Valor válido! sexo {sexo} registrado com sucesso!')
