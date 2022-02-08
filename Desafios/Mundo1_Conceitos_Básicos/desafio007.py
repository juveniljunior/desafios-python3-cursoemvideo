# ALGORITMO QUE LÊ DUAS NOTAS E MOSTRA A MÉDIA DELAS

n1 = float(input("\33[36mDigite a primeira nota: "))
n2 = float(input('\33[37mDigite a segunda nota: '))
media = (n1+n2)/2

print(f'\33[32mA média das notas \33[1;4;33m{n1:.1f}\33[32m e \33[1;4;33m{n2:.1f}\33[32m é igual a : \33[1;4;33m{media:.1f}')
