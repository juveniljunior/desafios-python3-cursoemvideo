# MAIOR E MENOR VALORES LIDOS
contador = soma = 0
resposta = ''
n = float(input('Digite um valor: '))
listadenumeros = [n]
soma += n
contador += 1
while resposta != 'N':
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'S':
        n = float(input('Digite um valor: '))
        listadenumeros += [n]
        soma += n
        contador += 1
    if resposta != 'S' and resposta != 'N':
        print('\33[31;1mResposta inválida. Tente novamente!\33[m')
print(f'\nVOCÊ DIGITOU {contador} NÚMEROS!\nSOMA ENTRE ELES = {soma:.0f}\nMÉDIA ENTRE ELES = {soma / contador:.2f}\n'
      f'MAIOR VALOR = {max(listadenumeros)}\nMENOR VALOR = {min(listadenumeros)}')
