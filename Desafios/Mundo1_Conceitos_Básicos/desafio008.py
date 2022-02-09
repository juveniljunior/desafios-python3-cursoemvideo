"""
Exercício Python 008:
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""

m = float(input('\33[31mEscreva o valor em metros: '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000
print(f'A medida de {m}m corresponde a: \n'
      f'\33[1;35m{km}km \n'
      f'{hm}hm \n'
      f'{dam}dam \n'
      f'{dm:0f}dm \n'
      f'{cm:.0f}cm \n'
      f'{mm:.0f}mm')
