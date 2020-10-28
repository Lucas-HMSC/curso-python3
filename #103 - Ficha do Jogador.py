def ficha(nome, gols):
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    if nome.strip() != '':
        print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
    else:
        nome = '<desconhecido>'
        print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


print('='*30)
nome = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols: '))
ficha(nome, gols)
