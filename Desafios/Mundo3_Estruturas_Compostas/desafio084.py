# LISTA COMPOSTA E ANÁLISE DE DADOS
galera = list()
dados = list()
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')).title())
    dados.append(float(input('Peso: ')))
    galera.append(dados[:])
    dados.clear()
    resposta = ''
    while resposta != 'N' and resposta != 'S':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'{"-="*30}\nAo todo, você cadastrou {len(galera)} pessoas.')
for p in galera:
    if galera.index(p) == 0:
        maior = menor = p[1]
    else:
        if p[1] > maior:
            maior = p[1]
        if p[1] < menor:
            menor = p[1]
print(f'O maior peso foi o de {maior}Kg. Peso de ', end='')
for p in galera:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso foi o de {menor}Kg. Peso de ', end='')
for p in galera:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
