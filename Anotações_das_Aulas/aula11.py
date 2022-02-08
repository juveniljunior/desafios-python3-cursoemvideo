nome = input('Qual seu nome? ').strip().title()
if nome == 'Junior':
    print(f'Seu nome é o mais bonito de todos!')
elif nome in 'José Maria Paulo Ana':
    print('Seu nome é bem popular viu!')
elif nome == 'Amanda' and 'Lourdes':
    print('Seu nome feminino é muitooo lindo!')
elif nome == 'Wall Enderson':
    print('Seu nome éo mais estranho que já vi!')
else:
    print(f'Seu nome é bem normalzinho!')
print(f'Tenha um bom dia, {nome}!')
