"""
Exercício Python 015:
Escreva um programa que pergunte a quantidade de
Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

"""

aluguel = float(input('\33[1;37mQuantos dias você usou o carro? '))
km = float(input('\33[1;97mQuantos kilômetros você percorreu? '))

pag = (aluguel * 60)+(km * 0.15)
print(f'\33[33mO valor a ser cobrado é: \33[1;34m{pag:.2f} R$.')
