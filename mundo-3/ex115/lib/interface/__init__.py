def leiaInt(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print('\033[31mERRO! digite um valor inteiro válido.\033[0m')


def linha(l=42):
    return '-' * l


def escreva(msg, l=42):
    print(linha(l))
    print(f'{msg}'.center(l))
    print(linha(l))


def menu(lista):
    escreva('SISTEMA DE CADASTRO')
    c = 1
    for item in lista: 
        print(f'\033[33m{c}\033[0m - \033[34m{item}\033[0m')
        c += 1
    print(linha())
    return leiaInt('\033[32mDigite sua opção:\033[0m ')
