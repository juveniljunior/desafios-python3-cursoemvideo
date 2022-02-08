# CONVERSOR DE BASES NUMÉRICAS

numero = int(input('Informe um número inteiro: '))
base = int(input(f'\33[35;1m[1] Binário\n'
                 f'\33[37m[2] Octal\n'
                 f'\33[32m[3] Hexadecimal\n\33[m'
                 f'Selecione para qual base quer converter: '))

if base == 1:
    print(f'O número {numero} na base \33[35;1mBINÁRIA\33[m é {numero:0b}')
elif base == 2:
    print(f'O número {numero} na base \33[37;1mOCTAL\33[m é {numero:0o}')
elif base == 3:
    print(f'O número {numero} na base \33[32;1mHEXADECIMAL\33[m é {numero:X}')
else:
    print('Você inseriu um valor \33[31;1mINVÁLIDO\33[m!')
