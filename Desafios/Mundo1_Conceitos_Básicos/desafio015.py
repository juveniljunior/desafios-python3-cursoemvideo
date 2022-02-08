# ALUGUEL DE UM CARRO

aluguel = float(input('\33[1;37mQuantos dias você usou o carro? '))
km = float(input('\33[1;97mQuantos kilômetros você percorreu? '))

pag = (aluguel * 60)+(km * 0.15)
print(f'\33[33mO valor a ser cobrado é: \33[1;34m{pag:.2f} R$.')
