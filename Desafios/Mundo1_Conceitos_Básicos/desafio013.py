"""
Exercício Python 013:
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""

salario = float(input('\33[1;33mDigite o valor atual do seu salário(R$): \33[m'))
novo = salario+(salario*15/100)
economia = salario*15/100

print(f'Um funcionário que ganhava \33[1;31m{salario}R$\33[m agora com \n'
      f'seu novo salário com aumento de 15% será: \33[1;34m{novo} R$\33[m')
print(f'Aumento de: \33[1;36m{economia:.2f} R$')
