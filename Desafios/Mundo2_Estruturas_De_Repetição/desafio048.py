# SOMA IMPÁRES MÚLTIPLOS DE TRÊS
s = 0
np = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        np += 1
print(f'A soma de todos os {np} números que são múltiplos de 3 de 1 a 500 é igual a {s}.')
