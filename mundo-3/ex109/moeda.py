def moeda(p = 0, moeda = 'R$'):
    '''
    -> formata um valor para um formato monetário
    :param p: o preço a ser formatado
    :param moeda: a sigla da moeda
    :return: string do preço formatado
    '''
    return f'{moeda}{p:.2f}'.replace('.', ',')


def dobro(p = 0, f=False):
    '''
    -> dobra um valor
    :param p: o preço a ser dobrado
    :param f: liga e desliga a formatação
    :return: o preço dobrado
    '''
    res = p * 2
    return res if not f else moeda(res)


def metade(p = 0, f=False):
    '''
    -> divide um valor pela metade
    :param p: o preço a ser dividido
    :param f: liga e desliga a formatação
    :return: o preço dividido pela metade
    '''
    res = p / 2
    return res if not f else moeda(res)


def aumentar(p = 0, qtd = 0, f=False):
    '''
    -> aumenta um valor por uma porcentagem
    :param p: o preço a ser aumentado
    :param qtd: a porcentagem
    :param f: liga e desliga a formatação
    :return: o preço aumentado
    '''
    res = p + (p * qtd / 100)
    return res if not f else moeda(res)


def diminuir(p = 0, qtd = 0, f=False):
    '''
    -> diminui um valor por uma porcentagem
    :param p: o preço a ser diminuido
    :param qtd: a porcentagem
    :param f: liga e desliga a formatação
    :return: o preço dimiduido
    '''
    res = p - (p * qtd / 100)
    return res if not f else moeda(res)
