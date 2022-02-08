"""num = [2, 9, 7, 4]
num[3] = 5
num.append(8)
num.sort(reverse=True)
num.insert(0, 2)
if 9 in num:
    num.remove(9)
else:
    print('Não achei o número 3.')
# num.pop(2)
print(num)
print(f'Esta lista tem {len(num)} elementos')

valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

# for v in valores:
    # print(f'{v}...', end=' ')
for c, v in enumerate(valores):
    print(f'O valor {v} está na posição {c}.')
print('Cheguei ao final da lista.')

a = [2, 5, 7, 9]
b = a[:]
b[3] = 10
print(f'Lista A: {a}')
print(f'Lista B: {b}')"""
# MOSTRA LISTA SEM PRECISAR USAR O FOR
names = ['Ellen', 'Tiago', 'Willian']
print(*names, sep=', ')
