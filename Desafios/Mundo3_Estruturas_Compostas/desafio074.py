from random import randint
numerossorteados = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram:', end=' ')
for c in range(0, len(numerossorteados)):
    print(f'{numerossorteados[c]}', end=' ')
print(f'\nOs maior valor sorteado foi {max(numerossorteados)}.\nO menor valor sorteado foi {min(numerossorteados)}.')
