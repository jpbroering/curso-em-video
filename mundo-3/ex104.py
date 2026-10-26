def leiaInt(mensagem=''):
    while True:
        resposta = input(mensagem)
        if resposta.isdigit():
            return int(resposta)
        print('\033[0;31mERRO! Digite um número inteiro válido.\033[0;0m')

n = leiaInt('Escreva n: ')
print(f'Você digitou o número {n}')