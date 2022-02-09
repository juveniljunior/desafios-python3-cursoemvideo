"""
Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o
usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
"""

print(f'{"="*40}\n{" LOJAS HIPER BARATÃO ":-^40}\n{"="*40}')
total = produtoscaros = 0
produtomaisbarato = []
nomedomaisbarato = ' '
while True:
    nomedoproduto = str(input('Nome do produto: ')).title()
    preco = float(input('Preço: R$ '))
    produtomaisbarato += [preco]
    total += preco
    if preco > 1000:
        produtoscaros += 1
    if min(produtomaisbarato) == preco:
        nomedomaisbarato = nomedoproduto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'{"FIM DO PROGRAMA":=^40}\nTotal da compra: R$ {total:.2f}\nTivemos {produtoscaros} produtos com valor de mais de R$ 1000.00\nO nome do produto mais barato foi {nomedomaisbarato} custando R$ {min(produtomaisbarato):.2f}')
