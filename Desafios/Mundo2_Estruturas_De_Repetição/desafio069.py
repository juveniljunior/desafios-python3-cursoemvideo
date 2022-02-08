# ANÁLISE DE DADOS DO GRUPO
maioresdeidade = homens = novinhas = 0
while True:
    print(f'{"="*40}\n{" CADASTRE UM PESSOA ":-^40}\n{"="*40}')
    idade = int(input('Idade: '))
    if idade > 18:
        maioresdeidade += 1
    sexo = ' '
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if sexo == 'M':
            homens += 1
        elif sexo == 'F' and idade < 20:
            novinhas += 1
    resposta = ' '
    while resposta != 'N' and resposta != 'S':
        resposta = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'{"="*40}\nAo todo {maioresdeidade} pessoas tem mais de 18 anos.\n{homens} homem(ns) se cadastraram.\n{novinhas} mulher(es) tem menos de 20 anos.')
