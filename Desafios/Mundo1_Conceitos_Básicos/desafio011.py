"""
Exercício Python 011:
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e
a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
"""

a = float(input('\33[1;31mDigite o valor da altura: '))
l = float(input('\33[1;33mDigite o valor da largura: '))
area = a*l
qt = area/2
print(f"\33[1;31mA dimensão da parede é \33[1;36m{a}x{l}\33[m\33[1;31m, a área da parede é \33[1;36m{area}m² \n "
      f"\33[1;31me são necessários \33[1;36m{qt:.2f} litros\33[1;31m de tinta para pintar a parede.")
