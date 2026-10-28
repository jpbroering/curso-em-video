def leiaInt(mensagem=''):
    while True:
        try:
            resposta = int(input(mensagem))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[0m')
        except KeyboardInterrupt:
            print('\n\033[0;31mUsuário preferiu não informar este número.\033[0m')
            return 0
        else:
            return resposta

def leiaFloat(mensagem=''):
    while True:
        try:
            resposta = float(input(mensagem))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número real válido.\033[0m')
        except KeyboardInterrupt:
            print('\n\033[0;31mUsuário preferiu não informar este número.\033[0m')
            return 0
        else:
            return resposta

n = leiaInt('Escreva um número inteiro: ')
r = leiaFloat('Escreva um número real: ')
print(f'Você digitou o número inteiro {n}')
print(f'Você digitou o número real {r}')