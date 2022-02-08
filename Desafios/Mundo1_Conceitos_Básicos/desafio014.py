# CONVERSOR DE TEMPERATURA
c = float(input('\33[33mInforme a temperetura em °C: '))
f = c*1.8+32
k = c+273

print(f'A temperatura de \33[1;32m{c}°C\33[33m corresponde a:'
      f' \33[1;32m{f}°F\33[33m e \33[1;32m{k}K.')
