# JOGO DA ADVINHAÇÃO 2.0
from random import randint
comp = randint(0, 10)
usu = 11
tent = 0
print('Sou o computador, acabei de pensar em um número entre 0 e 10!\nSerá se você consegue advinhar?')
while usu != comp:
    usu = int(input('Digite seu palpite: '))
    if usu < comp:
        print('\33[37;1mMAIS...\33[31;1mTente novamente!\33[m')
        tent += 1
    elif usu > comp:
        print('\33[37;1mMENOS...\33[31;1mTente novamente!\33[m')
        tent += 1
print(f'\33[34;1mPARABÉNS! Você advinhou o número que pensei!\n\33[37;1mPrecisou de {tent} tentativa(s) para acertar!')
