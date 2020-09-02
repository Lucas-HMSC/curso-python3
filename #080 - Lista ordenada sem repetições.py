from random import randint
from time import sleep
numeros = list()

while len(numeros) != 5:
    c = 0
    num = randint(0, 11)
    print(f'Valor gerado -> {num}')

    if num not in numeros:
        if c == 0 or num > numeros[-1]:
            numeros.append(num)
            print('Adicionado ao final da lista.')
            c += 1
            sleep(0.5)
        else:
            pos = 0
            while pos < len(numeros):
                if num < numeros[pos]:
                    numeros.insert(pos, num)
                    print(f'Adicionado na posição {pos} da lista.')
                    c += 1
                    break
                pos += 1
    else:
        print('Número repetido não será adicionado.')
print(numeros)
