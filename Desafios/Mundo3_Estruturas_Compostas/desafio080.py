# LISTA ORDENADA SEM REPETIÇÕES
lista = []
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > max(lista):
        lista.append(num)
        print('Valor adicionado no final da lista...')
    else:
        for p, v in enumerate(lista):
            if num <= v:
                lista.insert(p, num)
                print(f'Valor adicionado na posição {p} da lista...')
                break
print(f'{"-="*30}\nOs valores digitados em ordem são {lista}.')
