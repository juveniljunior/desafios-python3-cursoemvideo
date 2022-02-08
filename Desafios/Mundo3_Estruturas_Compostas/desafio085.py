# LISTA COM PARES E ÍMPARES
numeros = [[], []]
for c in range(1, 8):
    n = int(input(f'DIGITE O {c}º VALOR: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
numeros[0].sort()
numeros[1].sort()
print(f'{"+="*30}\nVALORES PARES DIGITADOS: {numeros[0]}')
print(f'VALORES ÍMPARES DIGITADOS: {numeros[1]}')
