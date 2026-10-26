

def voto(nascimento):
    from datetime import date
    ano = date.today().year
    idade = ano - nascimento
    if idade >= 18 and idade < 65:
        return f'Com {idade} anos: VOTO OBRIGARÓRIO.'
    elif idade >= 16 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    return f'Com {idade} anos: NÃO VOTA.'

print('-' * 20)
data = int(input('Em que ano você nasceu? '))
print(voto(data))