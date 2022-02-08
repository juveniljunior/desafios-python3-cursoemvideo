"""print(f'{"-"*40}\n{"LISTAGEM DE PREÇOS":^40}\n{"-"*40}')
lista = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20,
                          'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livros', 34.90)
print(f'{lista[0]:.<30}R${lista[1]:>8.2f}\n'
      f'{lista[2]:.<30}R${lista[3]:>8.2f}\n'
      f'{lista[4]:.<30}R${lista[5]:>8.2f}\n'
      f'{lista[6]:.<30}R${lista[7]:>8.2f}\n'
      f'{lista[8]:.<30}R${lista[9]:>8.2f}\n'
      f'{lista[10]:.<30}R${lista[11]:>8.2f}\n'
      f'{lista[12]:.<30}R${lista[13]:>8.2f}\n'
      f'{lista[14]:.<30}R${lista[15]:>8.2f}\n'
      f'{lista[16]:.<30}R${lista[17]:>8.2f}')"""
lista = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas', 22.30, 'Livros', 34.90)
print(f'{"-"*40}\n{"LISTAGEM DE PREÇOS":^40}\n{"-"*40}')
for pos in range(0, len(lista)):
      if pos % 2 == 0:
            print(f'{lista[pos]:.<30}', end=' ')
      else:
            print(f'R$ {lista[pos]:>7.2f}')

