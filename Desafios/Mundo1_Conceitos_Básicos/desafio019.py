# SORTEIO DE ALUNOS

import random
a1 = input('\33[34mDigite o nome do 1° aluno: ')
a2 = input('\33[33mDigite o nome do 2° aluno: ')
a3 = input('\33[32mDigite o nome do 3° aluno: ')
a4 = input('\33[31mDigite o nome do 4° aluno: ')
aluno_sorteado = [a1, a2, a3, a4]
print(f'\n \33[37mO aluno escolhido foi \33[1;4;97m{random.choice(aluno_sorteado)}\33[m\33[37m !')
