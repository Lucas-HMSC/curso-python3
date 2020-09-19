from random import randint
from time import sleep
jogos = []
jogo = []
option = int(input('Quantos jogos deseja gerar? '))
sleep(0.5)
print(f'GERANDO {option} JOGOS')
sleep(0.5)
for d in range(0, option):
    for c in range(0, 6):
        while True:
            aleat = (randint(1, 60))
            if aleat not in jogo:
                jogo.append(aleat)
                break
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()

for i, j in enumerate(jogos):
    print(f'Jogo {i+1}: {j}')
    sleep(0.5)
print('*'*5, '{:^11}'.format('BOA SORTE'), '*'*5)
