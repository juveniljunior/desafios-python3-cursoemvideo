"""
Exercício Python 055:
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

"""
lista = []  # Lista vazia
for p in range(1, 6):
    peso = float(input(f'Peso da {p}º pessoa: '))
    lista.append(peso)  # Adioiona os valores na lista (poderia ser também: lista += [peso])
print(f'O maior peso lido é {max(lista)}Kg e o menor é {min(lista)}Kg.')
