"""
Exercício Python 051:
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10
primeiros termos dessa progressão.
"""

print('='*30)
print(f'{" 10 TERMOS DE UMA PA ":=^30}')
print('='*30)
t1 = int(input('Digite o 1º termo da PA: '))
r = int(input('Digite a razão da PA: '))
for c in range(0, 9):
    t1 += r
    print(t1, end=' => ')
print('ACABOU')

