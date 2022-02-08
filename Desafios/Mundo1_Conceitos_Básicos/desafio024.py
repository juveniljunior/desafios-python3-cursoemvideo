# VERIFICANDO AS PRIMEIRAS LETRAS DE UM TEXTO

city = str(input('\33[32mEm que cidade você mora? ')).strip().capitalize()
print(f'A sua cidade começa com "Santo"? \nResposta: \33[1;4;34m{city.startswith("Santo")}')
