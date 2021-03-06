# SIMULADOR DE CAIXA ELETRÔNICO
"""
Exercício Python 071:
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""

print(f'{"="*30:^30}\n{" BANCO JUNIORBANK ":-^30}\n{"="*30:^30}')
valor = int(input('Qual valor você quer sacar?R$ '))
while True:
    if valor // 50 > 0:
        print(f'Total de {valor // 50} cédulas de R$ 50.')
        valor = valor - ((valor // 50) * 50)
    if valor // 20 > 0:
        print(f'Total de {valor // 20} cédulas de R$ 20.')
        valor = valor - ((valor // 20) * 20)
    if valor // 10 > 0:
        print(f'Total de {valor  // 10} cédulas de R$ 10.')
        valor = valor - ((valor // 10) * 10)
    if valor // 1 > 0:
        print(f'Total de {valor // 1} cédulas de R$ 1.')
    print('='*30)
    break
print('Volte sempre ao BANCO JUNIORBANK! Tenha um bom dia!')
