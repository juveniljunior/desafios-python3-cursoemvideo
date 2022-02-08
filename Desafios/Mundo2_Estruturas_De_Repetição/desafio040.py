# SITUAÇÃO FINAL DE UM ALUNO

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
