def ficha(nome='<desconhecido>', gols='0'):
    if len(nome) < 1:
        nome = '<desconhecido>'
    if len(gols) < 1:
        gols = '0'
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


print('-'*20)
nome = input('Nome do Jogador: ')
gols = input('Número de Gols: ')

print(ficha(nome, gols))