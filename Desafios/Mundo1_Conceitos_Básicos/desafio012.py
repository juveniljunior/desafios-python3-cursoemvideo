# DESCONTO DE UM PRODUTO

preço = float(input("\33[33mDigite o preço do produto(R$): "))
novo = preço - (preço*5/100)
economia = (preço*5/100)

print(f"O novo preço desse produto com valor de \33[1;31m{preço} R$ \n "
      f"\33[33mcom desconto de 5% será de: \33[1;31m{novo:.2f} R$")
print(f'\33[33mEconomia de: \33[1;31m{economia:.2f} R$')

# pp = float(input("Digite o preço do produto(R$): "))
# vp = pp*5/100
# vd = pp - vp
# print(f"O novo preço desse produto com valor de {pp} R$ \n com desconto de 5% será de: {vd:.2f} R$")
# print(f'Economia de: {vp:.2f} R$')