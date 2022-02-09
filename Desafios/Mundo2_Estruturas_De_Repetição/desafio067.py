# TABUADA v3.0
"""
Exercício Python 067:
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""

contador = num = 0
while True:
    num = int(input('Você quer ver a tabuada de que número? '))
    if num < 0:
        break
    contador = 1
    while contador <= 10:
        print(f'{num} X {contador:2} = {num * contador:2}')
        contador += 1
    """for contador in range(1, 11):
        print(f'{num} X {contador:2} = {num*contador:2}')"""
print('PROGRAMA TABUADA ENCERRADO COM SUCESSO!\nVolte sempre!')
