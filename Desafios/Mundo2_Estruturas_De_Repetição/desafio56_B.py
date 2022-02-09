# ANALISADOR COMPLETO
s = 0
sm = 0
for c in range(1, 5):
    print('='*25)
    nome = str(input('Digite seu nome: ')).strip().title()
    idade = int(input('Digite quantos anos você tem: '))
    sexo = int(input('[1] P/ HOMEM [2] P/ MULHER\nQual é seu sexo? '))
    s = s + idade
    if c == 1:
        nome1 = nome
        idade1 = idade
        sexo1 = sexo
    if c == 2:
        nome2 = nome
        idade2 = idade
        sexo2 = sexo
    if c == 3:
        nome3 = nome
        idade3 = idade
        sexo3 = sexo
    if c == 4:
        nome4 = nome
        idade4 = idade
        sexo4 = sexo

media = s / 4
print(f'A média entre as idades é de {media} anos.')
if sexo1 == 1 and idade1 > idade2 and idade1 > idade3 and idade1 > idade4:
    print(f'O homem mais velho é {nome1}.')
if sexo2 == 1 and idade2 > idade1 and idade2 > idade3 and idade2 > idade4:
    print(f'O homem mais velho é {nome2}.')
if sexo3 == 1 and idade3 > idade1 and idade3 > idade2 and idade3 > idade4:
    print(f'O homem mais velho é {nome3}.')
if sexo4 == 1 and idade4 > idade1 and idade4 > idade2 and idade4 > idade3:
    print(f'O homem mais velho é {nome4}')
if sexo1 == 2 and idade1 < 20:
        sm = sm + 1
if sexo2 == 2 and idade2 < 20:
        sm = sm + 1
if sexo3 == 2 and idade3 < 20:
        sm = sm + 1
if sexo4 == 2 and idade4 < 20:
        sm = sm + 1
if sexo1 == 2 or sexo2 == 2 or sexo3 == 2 or sexo4 == 2:
    print(f'{sm} mulher(es) tem menos de 20 anos.')
