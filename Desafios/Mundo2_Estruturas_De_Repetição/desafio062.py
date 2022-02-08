# SUPER PROGRESSÃO ARITMÉTICA v3.0
contador = 0
novocontador = 1
nc = 1
termos = 0
primeirotermo = int(input('1º TERMO DA PA: '))
razao = int(input('RAZÃO DA PA: '))
print(f'{primeirotermo} → ', end='')
while contador < 9:
    primeirotermo += razao
    contador += 1
    termos += 1
    print(f'{primeirotermo} → ' if contador < 9 else f'{primeirotermo}...', end='')
while novocontador > 0:
    novocontador = int(input('\nDIGITE QUANTOS TERMOS QUER MOSTRAR A MAIS (0 = PARAR): '))
    nc = novocontador
    novocontador = 0
    while novocontador < nc:
        primeirotermo += razao
        novocontador += 1
        termos += 1
        print(f'{primeirotermo} → ' if novocontador < nc else f'{primeirotermo}...', end='')
print(f'PROGRESSÃO FINALIZADA COM {termos + 1} TERMOS MOSTRADOS COM SUCESSO!')
