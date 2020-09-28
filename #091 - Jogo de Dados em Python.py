from random import randint
from time import sleep
from operator import itemgetter
jogadas = {
    'Jogador 1': randint(1, 6),
    'Jogador 2': randint(1, 6),
    'Jogador 3': randint(1, 6),
    'Jogador 4': randint(1, 6)
}
ranking = list()
sleep(0.5)
print('Valores sorteados:')
sleep(0.5)
for n, j in jogadas.items():
    print(f'    O {n} tirou {j}')
    sleep(0.5)
print('Ranking dos jogadores:')

ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)

for i, num in enumerate(ranking):
    sleep(0.5)
    print(f'    {i+1}º Lugar: {num[0]} com {num[1]}')
sleep(0.5)
