def leiaDinheiro(valor):
    contneg = valorneg = 0
    valor = input('Digite o preço: R$').strip()
    if valor[0] == '-':
        contneg = 1
        valorneg = valor
        valor = valor.replace('-', '')
    while not valor.isnumeric() and (valor.count(',') == 0 or valor.count(',') > 1) and \
            (valor.count('.') == 0 or valor.count('.') > 1):
        print(f'\33[31;1mERRO! "{valor}" é um valor inválido!\33[m')
        valor = input('Digite o preço: R$')
        if valor[0] == '-':
            contneg = 1
            valorneg = valor
            valor = valor.replace('-', '')

    if contneg == 1:
        if valorneg[1:] == valor:
            valor = valorneg
    if valor.count(',') == 1:
        valor = valor.replace(',', '.')
    return float(valor)
