# nome=input('Qual é seu nome? ')
# print(f'Prazer em te conhecer {nome:20}!')

#n1 = int(input('Digite um valor: '))
#n2 = int(input('Digite outro valor: '))
# print(f'O valor da soma entre {n1} e {n2} é igual a {n1+n2}!')

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
a = n1+n2
s = n1-n2
m = n1*n2
d = n1/n2
di = n1//n2
p = n1**n2

print(f'A soma é {a},\n a subtração é {s},\n a divisão é {d:.2f}', end=" === ")
print(f'Divisão inteira {di}, a potência {p}')
