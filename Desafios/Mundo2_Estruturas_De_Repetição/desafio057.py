# VALIDAÇÃO DE DADOS
sexo = str(input('Qual seu sexo? M ou F? ')).upper().strip()[0]
while sexo not in 'FM':
    sexo = str(input('Dados inválidos! Qual seu sexo? M ou F? ')).upper().strip()[0]
print(f'Valor válido! sexo {sexo} registrado com sucesso!')
