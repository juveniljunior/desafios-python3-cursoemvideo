# COMPARANDO NÚMEROS

a = int(input('\33[31;1mPrimeiro valor: '))
b = int(input('\33[34;1mSegundo valor: '))
if a > b:
    print(f'\33[31mO PRIMEIRO VALOR que é {a} é maior!')
elif b > a:
    print(f'\33[34mO SEGUNDO VALOR que é {b} é maior!')
else:
    print('\33[97mNão existe VALOR maior, os dois são iguais!')
