"""
Exercício Python 066:
Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas
(desconsiderando o flag).
"""

contador = 0
soma = 0
resposta = ''
n = float(input('Digite um valor: '))
listadenumeros = [n]
soma += n
contador += 1
while resposta != 'N':
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'S':
        n = float(input('Digite um valor: '))
        listadenumeros += [n]
        soma += n
        contador += 1
    if resposta != 'S' and resposta != 'N':
        print('\33[31;1mResposta inválida. Tente novamente!\33[m\n')
print(f'\nVOCÊ DIGITOU {contador} NÚMEROS!\nSOMA ENTRE ELES = {soma:.0f}\nMÉDIA ENTRE ELES = {soma / contador:.1f}\n'
      f'MAIOR VALOR = {max(listadenumeros)}\nMENOR VALOR = {min(listadenumeros)}')
