import cadastro
from time import sleep

while True:
    cadastro.escreva('SISTEMA DE CADASTRO')
    print('\033[33m1\033[0m - \033[34mListar pessoas cadastradas\033[0m')
    print('\033[33m2\033[0m - \033[34mCadastrar nova Pessoa\033[0m')
    print('\033[33m3\033[0m - \033[34mSair do sistema\033[0m')
    print('-' * cadastro.largura)
    opt = cadastro.leiaInt('\033[32mDigite sua opção:\033[0m ')
    sleep(0.2)
    match opt:
        case 1:
            cadastro.listar()
        case 2:
            cadastro.cadastrar()
        case 3:
            cadastro.escreva('Saindo do programa... Obrigado!')
            break
        case _:
            print()
            print('\033[31mERRO! digite uma opção válida.\033[0m')
            print()
            sleep(0.6)
