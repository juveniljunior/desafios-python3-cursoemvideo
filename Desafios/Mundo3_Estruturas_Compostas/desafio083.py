"""
Exercício Python 083:
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo
deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""

expressao = [str(input('Digite a expressão: '))]
pilha = 0
for elementos in expressao:
    for elemento in elementos:
        if '(' in elemento:
            pilha += 1
        if pilha > 0:
            if ')' in elemento:
                pilha -= 1
        else:
            pilha += 1
if pilha == 0:
    print('\33[34;1mSua expresssão está válida!\33[m')
else:
    print('\33[31;1mSua expressão está errada!')
