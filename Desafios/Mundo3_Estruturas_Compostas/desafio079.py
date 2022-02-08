# VALORES ÚNICOS NA LISTA
valores = list()
while True:
    valor = int(input('Digite um número: '))
    valores.append(valor)
    if valores.count(valor) == 1:
        print('Valor adicionado com sucesso...')
    elif valores.count(valor) > 1:
        print('Valor duplicado! Não vamos adicionar...')
        valores.remove(valor)
    resposta = ''
    while resposta != 'S' and resposta != 'N':
        resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break
print(f'{"/=/"*20}\nVocê digitou os valores {sorted(valores)}')
