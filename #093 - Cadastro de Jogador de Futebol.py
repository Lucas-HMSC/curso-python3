from random import randint
from time import sleep
tot = 0
jogador = {
    'nome': str(input('Nome do Jogador: '))
}
gols = []
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for i in range(0, partidas):
    sleep(0.5)
    print(f'Quantos gols na partida {i+1}? ', end='')
    gols.append(randint(0, 3))
    tot += gols[i]
    print(gols[i])
jogador['gols'] = gols[:]
jogador['total'] = tot
sleep(0.5)
print('*='*30)
print(jogador)
print('*='*30)
for i, j in jogador.items():
    sleep(0.5)
    print(f'O campo {i} tem o valor {j}.')
sleep(0.5)
print('*='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, j in enumerate(gols):
    sleep(0.5)
    print(f'    => Na partida {i+1}, fez {j} gols.')
sleep(0.5)
print(f'Foi um total de {jogador["total"]} gols.')
