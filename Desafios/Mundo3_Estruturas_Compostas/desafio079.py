"""
Exercício Python 079:
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

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
