sal = float(input('\033[1;36mDigite o seu salário(R$): '))
aum_sal = sal + (sal*10/100)
aum_sal2 = sal + (sal*15/100)
if sal > 1250:
    print(f'\033[35mO seu salário de \033[1;4;31m{sal:.2f}R$\033[m \033[35mcom aumento de 10% será de \033[1;4;32m{aum_sal:.2f}R$\033[m.')
else:
    print(f'\033[33mO seu salário de \033[1;4;31m{sal:.2f}R$\033[m \033[33mcom aumento de 15% será de \033[1;4;32m{aum_sal2:.2f}R$\033[m.')
