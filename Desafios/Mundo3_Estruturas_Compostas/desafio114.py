"""
Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
"""

from requests import get

"""try:
    get('http://pudim.com.br/')
    print('\33[34mO site Pudim está acessível no momento!\33[m')
except:
    print('\33[31mO site Pudim não está acessível no momento!')"""


def checkInternet():
    try:
        get('http://google.com.br')
        return True

    except:
        return False


if checkInternet():
    print('Internet OK!')
else:
    print('Internet NÃO conectada!')
