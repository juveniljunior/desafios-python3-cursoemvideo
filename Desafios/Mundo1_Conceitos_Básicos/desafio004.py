"""
Exercício Python 004:
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
informações possíveis sobre ele.
"""

teste = input('\33[37mDigite qualquer informação: ')

print("\n")
print(f'\33[34mÉ do tipo primitivo: \33[4;1;35m{type(teste)}')
print(f'\33[34mÉ um número? \33[4;1;35m{teste.isnumeric()}')
print(f'\33[34mÉ alfabético? \33[4;1;35m{teste.isalpha()}')
print(f'\33[34mÉ uma informação vazia ou faz parte do ASCII? \33[4;1;35m{teste.isascii()}')
print(f'\33[34mÉ alfa-numéricos? \33[4;1;35m{teste.isalnum()}')
print(f'\33[34mSão dígito(s)? \33[4;1;35m{teste.isdigit()}')
print(f'\33[34mSão decimal(is)? \33[4;1;35m{teste.isdecimal()}')
print(f'\33[34mÉ um identificador válido? \33[4;1;35m{teste.isidentifier()}')
print(f'\33[34mEstão APENAS em letras minúsculas? \33[4;1;35m{teste.islower()}')
print(f'\33[34mSão caracteres imprimíveis? \33[4;1;35m{teste.isprintable()}')
print(f'\33[34mContém apenas espaços em branco? \33[4;1;35m{teste.isspace()}')
print(f'\33[34mEstá capitalizada? \33[4;1;35m{teste.istitle()}')
print(f'\33[34mEstão APENAS em letras maiúsculas? \33[4;1;35m{teste.isupper()}')

