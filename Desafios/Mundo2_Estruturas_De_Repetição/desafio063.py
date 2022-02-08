# SEQUÊNCIA DE FIBONACCI v1.0
print('======= SEQUÊNCIA DE FIBONACCI =======')
n = int(input('DIGITE QUANTOS TERMOS VOCÊ QUER MOSTRAR: '))  # numero de vezes que é mostrado a sequência
anterior = 0  # primeiro termo da sequência
proximo = 1  # segundo termo da sequência
contador = 1
print(f'{anterior} ➡' if n >= 1 else exit(), end='')
while n - 1 > contador:
    resultado = anterior + proximo  # anterior + proximo = resultado
    print(f' {resultado} ➡', end='')
    while n - 1 > contador:
        anterior = resultado  # número 'anterior' se transforma no resultado da soma anterior
        proximo = resultado - proximo  # proximo = antecessor do resultado
        resultado = anterior + proximo  # soma o resultado da soma anterior com o antecessor desse resultado
        contador += 1
        print(f' {resultado} ➡', end='')
print(' FIM')
