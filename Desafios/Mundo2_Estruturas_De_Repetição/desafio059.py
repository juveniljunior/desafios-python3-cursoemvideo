# CRIANDO UM MENU DE OPÇÕES
from time import sleep
opcao = 0
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
while opcao != 5:
    opcao = int(input(f'[ 1 ] SOMAR\n[ 2 ] MULTIPLICAR\n[ 3 ] MAIOR\n[ 4 ] NOVOS NÚMEROS\n[ 5 ] SAIR DO PROGRAMA\n'
                      f'Escolha uma opção: '))
    if opcao == 1:
        print('|=|' * 8)
        print(f'A soma de {n1} + {n2} é igual a {n1 + n2}.')
        print('|=|' * 8)
    elif opcao == 2:
        print(f'A multiplicação de {n1} X {n2} é igual a {n1 * n2}.')
        print('|=|' * 8)
    elif opcao == 3:
        print('|=|' * 8)
        if n1 == n2:
            print(f'{n1} e {n2} são iguais!')
        else:
            print(f'{max(n1, n2)} é maior que {min(n1, n2)}.')
        print('|=|' * 8)
    elif opcao == 4:
        print('|=|' * 8)
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
        print('|=|' * 8)
    else:
        print('\33[31mOpcão inválida! Tente novamente!\33[m')
print('SAINDO DO PROGRAMA...')
sleep(1)
print('PROGRAMA FINALIZADO!  VOLTE SEMPRE!')
