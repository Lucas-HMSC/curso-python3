from random import randint

numeros = [[], []]

for c in range(0, 7):
    aleat = randint(1, 20)
    print(f'Número sorteado: {aleat}')
    if aleat % 2 == 0:
        if aleat not in numeros[0]:
            numeros[0].append(aleat)
    else:
        if aleat not in numeros[1]:
            numeros[1].append(aleat)
numeros[0].sort()
numeros[1].sort()
print(f'Os números pares sorteados foram ', end='')
for n in numeros[0]:
    print(n, end=' ')
print(f'\nOs números ímpares sorteados foram', end=' ')
for n in numeros[1]:
    print(n, end=' ')
