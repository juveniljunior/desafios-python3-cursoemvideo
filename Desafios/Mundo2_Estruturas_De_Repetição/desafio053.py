"""
Exercício Python 053:
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
"""
"""frase = str(input('Digite um frase: ')).replace(' ', '').strip().upper()
frase_inv = frase[::-1]
print(f'Frase normal: {frase}')
print(f'Frase invertida: {frase_inv}')
if frase == frase_inv:
    print('\33[34;1mEsta frase É UM PALÍNDROMO!\33[m')
else:
    print('\33[31;1mEsta frase NÃO É UM PALÍNDROMO!')"""
frase = str(input('Digite um frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if junto == inverso:
    print('\33[34;1mEsta frase É UM PALÍNDROMO!\33[m')
else:
    print('\33[31;1mEsta frase NÃO É UM PALÍNDROMO!')