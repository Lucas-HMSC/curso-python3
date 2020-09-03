from random import randint

numeros = []
numPar = []
numImpar = []

while True:
    aleat = randint(0, 10)
    if aleat != 0:
        numeros.append(aleat)
    else:
        break
for num in numeros:
    if num % 2 == 0:
        numPar.append(num)
    else:
        numImpar.append(num)
print(f'A lista completa é {numeros}.')
print(f'A lista contendo apenas os números pares é {numPar}.')
print(f'A lista contendo apenas os números impares é {numImpar}')
