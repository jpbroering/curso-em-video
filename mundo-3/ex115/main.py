from lib.interface import *
from lib.arquivo import *
from time import sleep

arquivo = './cadastros.txt'
if not arquivoExiste(arquivo):
    print('ARQUIVO CRIADO COM SUCESSO'.center(42))

opcoes = ['Listar pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do sistema']
while True:
    opt = menu(opcoes)
    match opt:
        case 1:
            escreva('PESSOAS CADASTRADAS')
            listar(arquivo)
        case 2:
            escreva('NOVO CADASTRO')
            nome = str(input('Digite o nome da pessoa: ')).strip().capitalize()
            idade = leiaInt('Digite a idade da pessoa: ')
            cadastrar(arquivo, nome, idade)
        case 3:
            escreva('Saindo do programa... Obrigado!')
            break
        case _:
            print()
            print('\033[31mERRO! digite uma opção válida.\033[0m')
            print()
    sleep(2)