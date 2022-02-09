"""
Exercício Python 073:
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
"""

primeiros20br = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense',
                 'América-MG', 'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá',
                 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
print(f'LISTA DE TIMES DO BRASILEIRÃO\n{"=-"*15}\n{primeiros20br}')
print(f'{"-="*15}\nOS PRIMEIROS 5 COLOCADOS SÃO: {primeiros20br[0:5]}')
print(f'{"-="*15}\nOS 4 ÚLTIMOS SÃO: {primeiros20br[16:]}')
print(f'{"-="*15}\nTIMES EM ORDEM ALFABÉTICA: {sorted(primeiros20br)}')
print(f'{"-="*15}\nA CHAPECOENSE ESTÁ NA {primeiros20br.index("Chapecoense")+1}ª POSIÇÃO')
