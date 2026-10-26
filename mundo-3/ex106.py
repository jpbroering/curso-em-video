from time import sleep

c = (
    '\033[0m',      # Sem cores
    '\033[0;97;41m',# Vermelho
    '\033[0;97;44m',# Azul
    '\033[0;97;42m',# Verde
    '\033[7m'       # Branco
)

def escreva(msg, cor=0):
    sleep(0.5)
    l = len(msg) + 4
    print(c[cor], end='')
    print('~' * l)
    print(f'  {msg}  ')
    print('~' * l)
    print(c[0], end='')


def ajuda(com):
    escreva(f'acessando o manual do comando \'{com}\'', 2)
    print(c[4], end='')
    help(com)
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    escreva('SISTEMA DE AJUDA PyHELP', 3)
    comando = str(input('Função ou Biblioteca > ')).strip()
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
escreva('ATÉ LOGO!', 1)