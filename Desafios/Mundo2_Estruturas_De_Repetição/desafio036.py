"""
Exercício Python 036:
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o
valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do
salário ou então o empréstimo será negado. """

valorcasa = float(input('Informe o valor da casa(R$): '))
salario = float(input('Informe o seu salário(R$): '))
anos = float(input('Informe em quantos anos você vai pagar a casa: '))
valormensal = valorcasa / (anos * 12)
print(f'Você pagará {valormensal:.2f}R$/mês para pagar a casa de {valorcasa:.2f}R$ em {anos:.0f} anos.')
if valormensal > 30/100*salario:
    print('\33[31;1mInfelizmente você NÃO poderá financiar a casa!\33[m')
else:
    print('\33[34;1mVocê PODERÁ financiar a casa!\33[m')
