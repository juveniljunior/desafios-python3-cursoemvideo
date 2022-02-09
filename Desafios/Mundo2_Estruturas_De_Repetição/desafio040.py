"""
Exercício Python 040:
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
"""

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print(f'Sua média foi {media}.')
if media < 5:
    print('\33[31;1mVocê está REPROVADO!\33[m')
elif 5 <= media < 7:
    print('\33[37;1mVocê irá para RECUPERAÇÃO!\33[m')
else:
    print('\33[34;1mPARABÉNS! Você está APROVADO!\33[m')
