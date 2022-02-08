"""nome = str(input('Qual é seu nome? '))
if nome == 'Junior':
    print(f'Que nome lindo você tem!\n'
          f'Bom dia, {nome}!')
else:
    print(f'Seu nome é tão normal!\n'
          f'Bom dia, {nome}!')"""

n1 = float(input('Digite sua 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))
n = (n1 + n2)/2
print(f'Sua média foi: {n:.1f}')
"""if n >=  6.0:
    print('Sua nota foi boa! PARABÉNS!')
else:
    print('Sua nota foi ruim! ESTUDE MAIS!')"""
print('PARABÉNS!' if n>=6 else 'ESTUDE MAIS!')
