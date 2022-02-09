"""
Exercício Python 043:
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
"""

n = str(input('Digite seu nome: ')).title()
m = float(input('Digite sua massa(kg): '))
a = float(input('Digite sua altura(m): '))
imc = m / a**2
print(f'Olá, {n}!')
print(f'Seu I.M.C é {imc:.2f}.')
if imc < 18.5:
    print('CUIDADO! Você está ABAIXO DO PESO!')
elif imc < 25:
    print('PARABÉNS! Você está com PESO IDEAL!')
elif imc < 30:
    print('CUIDADO! Você está em SOBREPESO!')
elif imc <= 40:
    print('CUIDADO REDOBRADO! Você apresenta OBESIDADE!')
else:
    print('CUIDADO REDROBADÍSSIMO! Você apresenta OBESIDADE MÓRBIDA!')
