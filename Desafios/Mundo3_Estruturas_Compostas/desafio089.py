"""
Exercício Python 089:
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""

from time import sleep
lista = list()
aluno = list()
notas = list()
media = 0
while True:
    aluno.append(str(input('Nome: ')).title())
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    media = (notas[0] + notas[1]) / 2
    aluno.append(notas[:])
    aluno.append(media)
    lista.append(aluno[:])
    notas.clear()
    aluno.clear()
    resposta = ''
    while resposta != 'S' and resposta != 'N':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'{"+="*20}\n{"Nº":<5}{"NOME":<15}{"MÉDIA":>20}\n{"+="*20}')
for dadoaluno in lista:
    print(f'{lista.index(dadoaluno):<5}{dadoaluno[0]:<15}{dadoaluno[2]:>20.1f}')
while True:
    notaal = int(input(f'{"+="*20}\nMostrar notas de qual aluno? [999 interrompe]: '))
    if notaal == 999:
        break
    else:
        for dadoaluno in lista:
            if notaal == lista.index(dadoaluno):
                print(f'{lista.index(dadoaluno):<5d} {dadoaluno[0]:<15s} {str(dadoaluno[1]):>20s}')
print(f'{"FINALIZANDO...":^20}')
sleep(3)
print(f'<<< VOLTE SEMPRE >>>')
