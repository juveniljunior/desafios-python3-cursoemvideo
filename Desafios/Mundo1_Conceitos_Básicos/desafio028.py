# JOGO DA ADVINHAÇÃO 1.0
# grupo https://chat.whatsapp.com/1wBTYJiFjcXGVWqW8XL8C8
from random import randint
from time import sleep
numcomp = randint(0, 5)
print('\033[30;41m-=-\033[m'*16)
print('\033[1;30;44mVOU PENSAR EM UM NÚMERO DE 0 A 5! TENTE ADVINHAR!\033[m')
print('\033[30;41m-=-\033[m'*16)
numusu = int(input('\033[35mEm que número pensei? '))
print('\033[1;36mPROCESSANDO...')
sleep(2)
if numusu == numcomp:
    print(f'\033[1;34mPARABÉNS! Você conseguiu me vencer!')
else:
    print(f'\033[31mGANHEI! O número que pensei foi \033[1;33m{numcomp}\033[m \033[31me não no \033[1;33m{numusu}.')
