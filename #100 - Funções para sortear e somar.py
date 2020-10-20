from random import randint
from time import sleep
numeros = []


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        aleat = randint(1, 10)
        lista.append(aleat)
        sleep(0.5)
        print(aleat, end=' ')
    sleep(0.5)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores de {lista}, temos {soma}.')


sorteia(numeros)
somaPar(numeros)
