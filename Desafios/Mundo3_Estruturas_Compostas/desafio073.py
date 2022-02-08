# TUPLAS COM TIMES DE FUTEBOL
primeiros20br = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense',
                 'América-MG', 'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá',
                 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
print(f'LISTA DE TIMES DO BRASILEIRÃO\n{"=-"*15}\n{primeiros20br}')
print(f'{"-="*15}\nOS PRIMEIROS 5 COLOCADOS SÃO: {primeiros20br[0:5]}')
print(f'{"-="*15}\nOS 4 ÚLTIMOS SÃO: {primeiros20br[16:]}')
print(f'{"-="*15}\nTIMES EM ORDEM ALFABÉTICA: {sorted(primeiros20br)}')
print(f'{"-="*15}\nA CHAPECOENSE ESTÁ NA {primeiros20br.index("Chapecoense")+1}ª POSIÇÃO')
