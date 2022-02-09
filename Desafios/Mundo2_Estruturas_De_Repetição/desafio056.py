"""
Exercício Python 056:
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do
grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

"""

velho = ''
idades = []
idadedoshomens = []
novinhas = 0
s = 0
for p in range(1, 5):
    print(f'{f" {p}º PESSOA ":=^30}')
    nome = str(input('Digite seu nome: ')).strip().title()
    idade = int(input('Digite quantos anos você tem: '))
    sexo = str(input('Qual é seu sexo? [M/F]? ')).upper()
    idades += [idade]
    s += idade
    if sexo == 'M':
        idadedoshomens += [idade]
        if idade == max(idadedoshomens):
            velho = nome
    if sexo == 'F' and idade < 20:
        novinhas += 1
print(f'A média entre as idades é de {s / 4} anos.')
print(f'O homem mais velho é {velho} que tem {max(idadedoshomens)} anos.')
print(f'{novinhas} mulher(es)tem menos de 20 anos.')
