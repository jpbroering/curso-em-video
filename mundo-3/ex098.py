from time import sleep


def contagem(i, f, p):
    inicio, fim, passo = i, f, p
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo *= -1

    print('-='*15)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio <= fim:
        while inicio <= fim:
            print(inicio, end=" ")
            inicio += passo
            sleep(0.25)
    else:
        while inicio >= fim:
            print(inicio, end=" ")
            inicio -= passo
            sleep(0.25)
    print('FIM!')
    print('-='*15)


contagem(1, 10, 1)
contagem(10, 0, -2)

print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(ini, fim, passo)