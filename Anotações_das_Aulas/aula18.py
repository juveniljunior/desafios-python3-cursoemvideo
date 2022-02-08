"""teste = []
teste.append('Junior')
teste.append(18)
familia = []
familia.append(teste[:])
teste[0] = 'Maria'
teste[1] = 48
familia.append(teste[:])
print(familia)"""
# ====================================
"""familia = [['Junior', 18], ['Rikellmy', 15], ['Rafael', 20]]
for p in familia:
    print(f'{p[0]} tem {p[1]} anos de idade.')"""
# ====================================
galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmen} maiores e {totmai} menores de idadee.')
