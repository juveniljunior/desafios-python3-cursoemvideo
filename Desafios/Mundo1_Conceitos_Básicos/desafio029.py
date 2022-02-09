"""Exercício Python 029:
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
"""

vel = float(input('\033[36mQual foi a velocidade do carro(Km/h)? '))
mul = (vel - 80.0) * 7.0
if vel > 80.0:
    print(f'\033[1;31mVOCÊ SERÁ MULTADO! limite de velocidade de \033[1;37m80km\h\033[1;31m excedido!\033[m\n'
          f'\033[32mVALOR DA MULTA: \033[1;7;97;40m{mul:.2f}R$\033[m')
else:
    print('\033[1;32mBom dia! Siga em frente com segurança!')
