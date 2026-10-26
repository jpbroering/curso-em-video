from random import randint
from time import sleep

num = []
def sorteia(lista):
    print('Sorteando 5 valores da lista:', end=' ')
    for _ in range(5):
        num = randint(1, 10)
        lista.append(num)
        print(num, end=' ')
        sleep(0.25)
    print('PRONTO!')

def somaPar(l):
    soma = 0
    print(f'Somando os valores pares de {l},', end=' ')
    for num in l:
        if num % 2 == 0:
            soma += num
    print(f'temos {soma}')

sorteia(num)
somaPar(num)