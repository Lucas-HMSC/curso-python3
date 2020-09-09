from random import randint

matriz = [[], [], []]

for l in range(0, 3):
    for c in range(0, 3):
        aleat = randint(0, 99)
        matriz[l].append(aleat)
        print(f'Número sorteado [{l}, {c}]: {aleat}')
for linha in matriz:
    for num in linha:
        print(f'[ {num:2} ]', end='')
    print()
