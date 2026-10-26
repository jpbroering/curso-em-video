def dobro(p = 0):
    return p * 2


def metade(p = 0):
    return p / 2


def aumentar(p = 0, qtd = 0):
    return p + (p * qtd / 100)


def diminuir(p = 0, qtd = 0):
    return p - (p * qtd / 100)


def moeda(p = 0, moeda = 'R$'):
    return f'{moeda}{p:.2f}'.replace('.', ',')
