"""lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')"""

"""for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}.')
print('Comi pra caramba!')"""

# ----------------------------------------------------------
"""lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(sorted(lanche))
print(lanche)"""
# ----------------------------------------------------------
"""a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.index(8))"""
# -----------------------------------------------------------
"""pessoa = ('Junior', 39, 'M', 60.50)
del(pessoa[0])
print(pessoa)"""

# -----------------------------------------------------------
palavras = ('aprender', 'programar', 'python', 'tecnologia', 'informação', 'internet')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos', end=' ')
    for letra in p:
        if letra in 'aeiou':
            print(f'{letra}', end=' ')
