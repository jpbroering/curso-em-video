
def leiaDinheiro(msg=''):
    '''
    -> Valida se a entrada até ser um valor decimal
    :param msg: Texto a ser mostrado
    :return: float
    '''
    while True:
        val = input(msg).strip().replace(',', '.')
        if not val.isalpha() and val != '':
            return float(val)
        print(f'\033[1;31mERRO: \"{val}\" é um preço inválido!\033[0m')