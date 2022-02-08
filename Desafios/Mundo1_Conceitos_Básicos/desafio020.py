# SORTEIO DE LISTA ORDENADA DE ALUNOS

import random
a1 = input('\33[34m1º aluno: ')
a2 = input('\33[33m2º aluno: ')
a3 = input('\33[32m3º aluno: ')
a4 = input('\33[31m4º aluno: ')
lista_de_nomes = [a1, a2, a3, a4]

random.shuffle(lista_de_nomes)
print(f'\33[1;97m{lista_de_nomes}')
