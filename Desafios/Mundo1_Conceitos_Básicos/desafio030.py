num = int(input('\033[33mDigte um número: \033[m'))
par = num % 2
if par == 0:
    print(f'\033[34mO NÚMERO \033[1;33m{num}\033[m \033[34mÉ PAR!')

else:
    print(f'\033[31mO NÚMERO \033[1;33m{num}\033[m \033[31mÉ IMPAR!')
