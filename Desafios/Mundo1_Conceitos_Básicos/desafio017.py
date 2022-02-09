"""Exercício Python 017:
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
triângulo retângulo. Calcule e mostre o comprimento da hipotenusa. """

from math import hypot
catopost = float(input('\33[1;34mDigite o cumprimento do cateto oposto: '))
catadj = float(input('\33[1;35mDigite o comprimento do cateto adjacente: '))
hip = hypot(catadj, catopost)
print(f'\33[37mO comprimento da hipotenusa é: \33[1;97m{hip:.2f}')

'''from math import pow, sqrt
catopost = float(input('Digite o cumprimento do cateto oposto: '))
catadj = float(input('Digite o comprimento do cateto adjacente: '))
hip = sqrt(pow(catopost,2)+pow(catadj,2))
print(f'O comprimento da hipotenusa é: {hip:.2f}')'''
