"""
Exercício Python 110:
Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
"""

import moeda
p = float(input('Digite o preço: R$'))
pa = int(input('Qual a porcentagem de aumento? '))
pd = int(input('Qual a porcentagem de diminuição? '))
moeda.resumo(p, pa, pd)
