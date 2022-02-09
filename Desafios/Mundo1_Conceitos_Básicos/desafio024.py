"""
Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
"""

city = str(input('\33[32mEm que cidade você mora? ')).strip().capitalize()
print(f'A sua cidade começa com "Santo"? \nResposta: \33[1;4;34m{city.startswith("Santo")}')
