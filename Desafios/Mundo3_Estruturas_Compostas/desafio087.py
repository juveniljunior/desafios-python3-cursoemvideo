"""
Exercício Python 087:
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""

matriz = list()
linha = list()
somap = maiorlin2 = 0
for c in range(0, 3):
    linha.append(int(input(f'Digite o valor para [{c}, 0]: ')))
    linha.append(int(input(f'Digite o valor para [{c}, 1]: ')))
    linha.append(int(input(f'Digite o valor para [{c}, 2]: ')))
    matriz.append(linha[:])
    linha.clear()
    c += 1
print('=+'*30)
print(f'[ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ]\n'
      f'[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ] \n'
      f'[ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2]} ]')
print('=+'*30)
for linha in matriz:
    for n in linha:
        if n % 2 == 0:
            somap += n
soma3col = matriz[0][2] + matriz[1][2] + matriz[2][2]
for n in matriz[1]:
    if n == matriz[1][0]:
        maiorlin2 = matriz[1][0]
    else:
        if n > maiorlin2:
            maiorlin2 = n
print(f'A soma dos valores é {somap}.\nA soma dos valores da 3ª coluna é {soma3col}.\nO maior valor da 2ª linha é {maiorlin2}.')
