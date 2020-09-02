from random import randint
numeros = list()
cont = val5 = 0
ver5 = False
while True:
    aleat = randint(0,10)
    if aleat != 0:
        numeros.append(aleat)
        cont += 1
        if aleat == 5:
            ver5 = True
            val5 += 1
    else:
        print('Algoritmo encerrado.')
        print(numeros)
        break
print(f'Foram digitados {cont} números.')
numeros.sort(reverse=True)
print('A lista de valores de forma ordenada decrescente é {}' .format(numeros))
if ver5:
    print(f'O número 5 faz parte da lista, foi encontrado {val5} vezes.')
else:
    print('O número 5 não foi encontrado na lista.')
