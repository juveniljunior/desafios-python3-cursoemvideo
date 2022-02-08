"""
Exercício Python 092:
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com
idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação
e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""

from datetime import date
anoatual = date.today().year
ficha = {'nome': str(input('Nome: ')).title(), 'idade': anoatual - int(input('Ano de Nascimento: ')),
         'ctps': int(input('Carteira de Trabalho (0 não tem): '))}
if ficha['ctps'] > 0:
    ficha['contratação'] = int(input('Ano de Contratação: '))
    ficha['salario'] = float(input('Salário: R$ '))
    ficha['aposentadoria'] = (ficha['contratação'] + 35) - (anoatual - ficha['idade'])
print("+=+"*10)
for k, v in ficha.items():
    print(f'{k} tem o valor de {v}')
