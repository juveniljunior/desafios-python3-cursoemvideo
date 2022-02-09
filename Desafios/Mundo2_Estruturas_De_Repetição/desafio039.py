"""
Exercício Python 039:
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua
idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do
alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import date
sexo = str(input('QUAL SEU SEXO? M ou F? ')).strip().upper()
if sexo == 'F':
    print('Você não precisa se alistar!')
if sexo == 'M':
    ano = int(input('ANO DE NASCIMENTO: '))
    idade = date.today().year - ano
    print(f'Você nasceu em {ano}, tendo {idade} anos em {date.today().year}.')

    if idade < 18:
        print(f'Você ainda irá se alistar!\n'
              f'Faltam {18 - idade} ano(s) para você se alistar!\n'
              f'Você se alistará em {ano + 18}.')
    elif idade == 18:
        print(f'Já é hora de se alistar!')
    else:
        print(f'Já passou da hora de se alistar!\n'
              f'Você passou {idade - 18} ano(s) do prazo de se alistar!\n'
              f'Você se alistou em {ano + 18}.')

