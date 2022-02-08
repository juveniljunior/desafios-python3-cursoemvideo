# PRIMEIRA E ÚLTIMA OCORRÊNCIA DE UMA STRING

phrase = str(input('\33[35mDigite uma frase: ')).strip().upper()
print(f'Nesta frase a letra "A" aparece \33[33;1;4m{phrase.count("A")} \33[35mvezes.\n'
      f'O "A" aparece pela 1° vez na posição \33[33;1;4m{phrase.find("A")+1}.\n'
      f'\33[35mO "A" aparece pela última vez na posição \33[33;1;4m{phrase.rfind("A")+1}\33[35m.')
