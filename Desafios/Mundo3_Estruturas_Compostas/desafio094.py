"""
Exercício Python 094:
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas
B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média
"""

listadepessoas = list()
somadeidades = 0
pessoa = dict()
while True:
    pessoa['nome'] = str(input('Nome: ')).title()
    pessoa['sexo'] = ' '
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('\33[1;31mERRO! Por favor, digite apenas M ou F.\33[m')
    pessoa['idade'] = int(input('Idade: '))
    somadeidades += pessoa['idade']
    listadepessoas.append(pessoa)
    continuar = ''
    while continuar != 'N' and continuar != 'S':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar != 'N' and continuar != 'S':
            print('\33[1;31mERRO! Por favor, digite apenas S ou N.\33[m')
    if continuar in 'Nn':
        break

mediadeidades = somadeidades / len(listadepessoas)
print(f'{"=+="*20}\n➽ O grupo tem {len(listadepessoas)} pessoas.')
print(f'➽ A média de idade é de {mediadeidades:.2f} anos.')
print(f'➽ As mulheres cadstradas foram: ', end='')
for pessoa in listadepessoas:
    for p in pessoa.values():
        if p == 'F':
            print(f'{pessoa["nome"]} ', end='')
print(f'\n➽ Lista de pessoas que estão acima da média:')
for pessoa in listadepessoas:
    if pessoa['idade'] > mediadeidades:
        for k, v in pessoa.items():
            print(f'{k} = {v}; ', end='')
        print()
print(f'{"<"*15} ENCERRADO {">"*15}')
