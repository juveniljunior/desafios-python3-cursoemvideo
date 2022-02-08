# EXTRAINDO DADOS EM UMA LISTA
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resposta = ''
    while resposta != 'N' and resposta != 'S':
        resposta = str(input('Quer continuar? {S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
valores.sort(reverse=True)
print(f'{"-="*25}\nVocê digitou {len(valores)} elementos.')
print(f'Os valores em ordem decrescente são {valores}.')
print('O valor 5 faz parte da lista!' if 5 in valores else 'O valor 5 não foi encontrado na lista!')
