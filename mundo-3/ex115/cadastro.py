largura = 75

def escreva(msg):
    print('-' * largura)
    print(f'{msg}'.center(largura))
    print('-' * largura)


def leiaInt(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print('\033[31mERRO! digite um valor inteiro válido.\033[0m')


def leiaNome(msg):
    while True:
        try:
            nome = str(input(msg))
            if len(nome) > 0 and len(nome) < largura // 2:
                return nome
            else:
                print(f'\033[31mERRO! digite um texto menor que {largura // 2}.\033[0m')
        except ValueError:
            print(f'\033[31mERRO! digite um texto válido.\033[0m')

def cadastrar():
    escreva('NOVO CADASTRO')
    with open('cadastros.txt', '+a') as file:
            nome = leiaNome('Digite o nome: ')
            idade = leiaInt('Digite a idade: ')
            file.write(f'{nome},{idade}\n')

# Função ou rotina
def listar():
    escreva('PESSOAS CADASTRADAS')
    with open('cadastros.txt', 'r') as file:
        while True:
            cadastro = file.readline()
            if cadastro == '':
                return
            cadastro = cadastro.split(',')
            if len(cadastro) != 2:
                continue
            print(f'{cadastro[0].center(largura // 2)}:{cadastro[1].center(largura // 2)}')
        