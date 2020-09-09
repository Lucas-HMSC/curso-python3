from random import randint
matriz = [[], [], []]
somaP = soma3 = maior2 = 0
for l in range(0, 3):
    for c in range(0, 3):
        aleat = randint(1, 9)
        matriz[l].append(aleat)
        print(f'Número sorteado [{l}, {c}]: {aleat}')
        if aleat % 2 == 0:
            somaP += aleat
        if c == 2:
            soma3 += aleat
        if l == 1:
            if l == 0:
                maior2 = aleat
            elif aleat > maior2:
                maior2 = aleat
print('='*20)
for linha in matriz:
    for num in linha:
        print(f'[{num:2} ]', end='')
    print()
print('='*20)
print(f'A soma de todos os valores pares digitados é {somaP}.')
print(f'A soma dos valores da terceira coluna é {soma3}.')
print(f'O maior valor da segunda linha é {maior2}.')
