from random import randint
from time import sleep
gols = []
jogador = {}
jogadores = list()
tot = flag = 0
while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for i in range(0, partidas):
        sleep(0.5)
        print(f'Quantos gols na partida {i+1}? ', end='')
        gols.append(randint(0, 3))
        tot += gols[i]
        print(gols[i])
    jogador['gols'] = gols[:]
    gols.clear()
    jogador['total'] = tot
    tot = 0
    jogadores.append(jogador.copy())
    option = str(input('Deseja continuar? [S/N] '))
    while option not in 'SsNn':
        option = str(input('Deseja continuar? [S/N] '))
    if option.strip() in 'Nn':
        break

sleep(0.5)
print('*='*30)
print(f'{"Cod":<4}', end='')
print(f'{"Nome":<10}', end='')
print(f'{"Gols":<10}', end='')
print(f'{"Total":^6}')
print('-'*30)
for i, j in enumerate(jogadores):
    print(f'{i:<4}', end='')
    for k in j.values():
        print(f'{str(k):<10}', end='')
    print()
print('-'*30)

while True:
    flag = int(input('Mostrar dados de qual jogador? 999 to STOP '))
    if flag == 999:
        break
    if flag >=  len(jogadores):
        print(f'ERRO! Nenhum jogador encontrado com o código {flag}.')
    else:
        print(f'== LEVANTAMENTO DO JOGADOR {jogadores[flag]["nome"]}:')
        for i, n in enumerate(jogadores[flag]['gols']):
            print(f'No jogo {i+1} fez {n} gols.')
