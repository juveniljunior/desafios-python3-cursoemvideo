"""
Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""

nome = input('\33[31mQual seu nome completo? ').strip().upper()
print(f'\33[32mVocê contém "Silva" no nome? \nResposta: \33[36;1m{"SILVA" in nome.split()}')
