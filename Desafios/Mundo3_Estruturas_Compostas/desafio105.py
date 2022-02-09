"""
Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
retornar um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
"""


def notas(*nota, sit=False):
    """
    => A função nota serve para mastrar o total de notas, a maior e a menor, média e situação do aluno.
    :param nota: recebe as notas do aluno
    :param sit: (opcional) mostra a situção do aluno de acordo com as notas fornecidas
    :return: dicionário com o total de notas, maior e menor nota, média entre elas e sua situaççao.
    """
    mai = men = somanotas = 0
    dictnotas = dict()
    for cont, n in enumerate(nota):
        somanotas += n
        if cont == 0:
            mai = men = n
        else:
            if n > mai:
                mai = n
            if n < men:
                men = n
        cont += 1
    dictnotas['Total'] = cont
    dictnotas['Maior'] = mai
    dictnotas['Menor'] = men
    dictnotas['Média'] = somanotas / dictnotas['Total']
    if sit:
        if dictnotas['Média'] >= 7:
            dictnotas['Situação'] = 'BOA'
        elif dictnotas['Média'] >= 5:
            dictnotas['Situação'] = 'RAZOÁVEL'
        else:
            dictnotas['Situação'] = 'RUIM'
    print(dictnotas)


# PROGRAMA PRINCIPAL
notas(5.5, 9.5, 10, 6.5, sit=True)
# help(notas)

