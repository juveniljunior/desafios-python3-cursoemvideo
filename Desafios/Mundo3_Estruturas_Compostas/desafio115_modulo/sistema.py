# SISTEMAS COM TODAS FUNÇÕES DO DESAFIO 115
def escreva(msg):
    print('\33[1;37m-'*40)
    print(f'{str(msg).center(40)}')
    print('\33[1;37m-\33[m' * 40)


def leiaNome(nome):
    while True:
        nome = input('Nome: ').strip()
        nomecomespacos = nome
        if nome.count(' ') > 0:
            nome = nome.replace(' ', '')
        if nome.isalpha():
            break
        else:
            print('\33[31;1mPor favor, digite um nome válido!\33[m')
    return nomecomespacos.title()


def leiIdade(valor):
    while True:
        try:
            valor = int(input('Idade: '))
            break
        except:
            print('\33[31;1mPor favor, digite um número válido!\33[m')
    return valor


def cadastroPessoa():
    escreva('NOVO CADASTRO')
    nome = leiaNome('Nome:')
    idade = leiIdade('Idade: ')
    file = open('PessoasCadastradas.txt', 'a')
    file.write(f'{nome:30}{idade:<3}{"anos":5}\n')
    file.close()
    print(f'Novo registro de {nome} foi adicionado.')


def listaPessoasCadastradas():
    arquivo = open('PessoasCadastradas.txt', 'r')
    escreva('PESSOAS CADASTRADAS')
    for pessoa in arquivo:
        print(f'{pessoa}', end='')
    arquivo.close()


def menuPrincipal():
    from time import sleep
    while True:
        sleep(2)
        escreva('MENU PRINCIPAL')
        print(f'\33[33m1 - \33[36mVer pessoas cadastradas\n'
              f'\33[33m2 - \33[36mCadastrar uma nova pessoa\n'
              f'\33[33m3 - \33[36mSair do Sistema\33[m\n\33[1;37m{"-"*40}')
        opcao = ''
        while not opcao.isnumeric():
            opcao = input('\33[33;1mSua opção: \33[m').strip()
            if opcao.isnumeric() and int(opcao) == 1:
                listaPessoasCadastradas()
            elif opcao.isnumeric() and int(opcao) == 2:
                cadastroPessoa()
            elif opcao.isnumeric() and int(opcao) == 3:
                escreva('SAINDO DO SISTEMA... ATÉ LOGO')
                sleep(1.5)
                break
            else:
                print('\33[31;1mERRO! Por favor, digite uma opção válida!\33[m')
        if int(opcao) == 3:
            break
