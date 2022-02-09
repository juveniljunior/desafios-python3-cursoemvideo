"""
Exercício Python 005:
Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

"""

num = int(input('\33[36mDigite um número: \33[m'))
print(f'O antecessor de \033[1;4;32m{num}\33[m é \033[1;4;32m{num-1}\33[m e o seu sucessor é \033[1;4;32m{num+1}')
