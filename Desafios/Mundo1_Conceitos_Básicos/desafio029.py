vel = float(input('\033[36mQual foi a velocidade do carro(Km/h)? '))
mul = (vel - 80.0) * 7.0
if vel > 80.0:
    print(f'\033[1;31mVOCÊ SERÁ MULTADO! limite de velocidade de \033[1;37m80km\h\033[1;31m excedido!\033[m\n'
          f'\033[32mVALOR DA MULTA: \033[1;7;97;40m{mul:.2f}R$\033[m')
else:
    print('\033[1;32mBom dia! Siga em frente com segurança!')
