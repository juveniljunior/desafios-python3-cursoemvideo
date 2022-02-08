print('\033[1;37m-=-' * 8)
print('\033[1;35m''ANALISADOR DE TRIÂNGULOS\033[m')
print('\033[1;37m-=-' * 8)
r1 = float(input('\033[34mDigite a medida do 1º seguimento do triângulo: '))
r2 = float(input('\033[32mDigite a medida do 2º seguimento do triângulo: '))
r3 = float(input('\033[33mDigite a medida do 3º seguimento do triângulo: \033[m'))

if r2 + r3 > r1 and r1 + r3 > r2 and r1 + r2 > r3:
    print('\033[1;36m\nÉ POSSÍVEL formar um triângulo com essas medidas.')
else:
    print('\033[1;31m\nNão é possível formar um triângulo com essas medidas.')
