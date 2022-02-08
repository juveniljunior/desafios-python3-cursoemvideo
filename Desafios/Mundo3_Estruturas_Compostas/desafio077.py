palavras = ('item', 'gratuito', 'proibido', 'rubrica', 'recorde', 'rudico')  # Tuplas das palavras a serem analisadas
for p in palavras:  # Para cada palavra da tupla
    print(f'\nNa palavra {p.upper()} temos ', end='')  # Palavra a ser analisada
    for letra in p:  # Para analisar cada letra de cada palavra da tupla
        if letra.lower() in 'aeiou':  # Se a letra(minúscula) for uma vogal
            print(letra, end=' ')  # Mostra a vogal dessa palavra uma pós outra
