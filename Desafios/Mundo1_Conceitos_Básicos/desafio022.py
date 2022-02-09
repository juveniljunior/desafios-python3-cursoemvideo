"""
Exercício Python 022:
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
"""

nome = str(input('\33[33mInforme o seu nome completo: ')).strip()
print(f'Analisando seu nome, temos...\n'
      f'\33[36mSeu nome completo em maiuscúlas é: \33[1;34m{nome.upper()}\n'
      f'\33[36mSeu nome completo em minúsculas é: \33[1;34m{nome.lower()}')
primeiro = nome.split()
print(f'\33[36mSeu nome completo tem \33[1;34m{len(nome.title()) - nome.count(" ")}\33[36m letras')
print(f'Seu primeiro nome é \33[1;34m{primeiro[0]} \33[36me tem {nome.find(" ")} \33[36mletras')


'''nome = str(input('Informe o seu nome completo: ')).strip()
print(f'Analisando seu nome, temos...\n'
      f'Seu nome completo em maiuscúlas é: {nome.upper()}\n'
      f'Seu nome completo em minúsculas é: {nome.lower()}')
nomej = nome.replace(" ", "")
print(f'Seu nome completo tem {len(nomej)} letras')
lista = nome.split()
print(f'Seu primeiro nome é {lista[0]} tem {len(lista[0])} letras')'''