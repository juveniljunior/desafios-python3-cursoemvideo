# GERENCIADOR DE PAGAMENTOS

print('--'*20)
print(f'{" LOJAS JUNIOR ":=^40}')
print('--'*20)
preco = float(input('Preço das compras (R$): '))
condicao = int(input(f'CONDIÇÕES:\n'
                     f'[1] A vista dinheiro/cheque\n'
                     f'[2] A vista no cartão\n'
                     f'[3] 2x no cartão\n'
                     f'[4] 3x ou mais no cartão\n'
                     f'Escolha uma condição de pagamento:  '))
if condicao == 1:
    print(f'O produto de  {preco:.2f}R$ com desconto de 10% custará {preco - (10/100*preco):.2f}R$')
elif condicao == 2:
    print(f'O produto de {preco:.2f}R$ com desconto de 5% custará {preco - (5/100*preco):.2f}R$')
elif condicao == 3:
    print(f'O produto continuará com o mesmo preço de {preco}R$ sem juros, \nMensalidade de 2X de R${preco/2:.2f}')
elif condicao == 4:
    parcela = int(input('Você quer parcelar em quantas vezes? '))
    print(f'O produto de preço {preco:.2f}R$ sofrerá 20% de juros e custará {preco + (preco * 20 / 100):.2f}R$\n'
          f'mensalidade de {parcela}X de {(preco + (preco * 20 / 100))/parcela:.2f}R$')
else:
    print('Condição de pagamento inválida!')
