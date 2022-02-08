# PROGRESSÃO ARITMÉTICA v2.0
contador = 0
primeirotermo = int(input('1º TERMO DA PA: '))
razao = int(input('RAZÃO DA PA: '))
novocontador = 1
print(f'{primeirotermo},', end='')
while contador < 9:
    primeirotermo += razao
    contador += 1
    print(f'{primeirotermo},' if contador < 9 else f'{primeirotermo}...', end='')
