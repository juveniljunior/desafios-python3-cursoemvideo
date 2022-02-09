"""
Exercício Python 041:
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
"""

from datetime import date
nasc = int(input('Ano de nascimento: '))
idade = date.today().year - nasc
print(f'Sua idade é de {idade} anos.')
if idade <= 9:
    print(f'Sua categoria é a MIRIM!')
elif idade <= 14:
    print(f'Sua categoria é a INFANTIL!')
elif idade <= 19:
    print('Sua categoria é a JUNIOR!')
elif idade <= 20:
    print('Sua categoria é a SÊNIOR!')
else:
    print('Sua categoria é MASTER!')
