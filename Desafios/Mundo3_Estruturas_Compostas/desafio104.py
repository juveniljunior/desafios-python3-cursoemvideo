"""
Exercício Python 104:
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')
"""


def leiaInt(num):
    num = input("Digite um número: ").strip()

    def isNumero(num):
        try:
            float(num)
            return True
        except:
            pass
            return False

    while (not isNumero(num)) or ((isNumero(num) == True) and (float(num) // 1.0 != float(num))):
        print(f'\33[31;1mERRO! Digite um número inteiro válido!\33[m')
        print('\33[37;1m-=\33[m' * 30)
        num = input('Digite um número: ')
    return num


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}!')
print('\33[37;1m-=\33[m' * 30)

