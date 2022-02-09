"""
Exercício Python 101:
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO
nas eleições.
"""


def voto(anodenascimento):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - anodenascimento
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        return 'NÃO VOTA'
    if 16 <= idade < 18 or idade > 65:
        return 'VOTO OPCIONAL '
    else:
        return 'VOTO OBRIGATÓRIO'


# PROGRAMA PRINCIPAL
resvoto = voto(int(input("Em que ano você nasceu? ")))
print(f'\33[36;1m{resvoto}\33[m')

