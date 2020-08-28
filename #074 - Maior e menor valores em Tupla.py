from random import randint
'''
*Jeito antigo e errado
num1 = randint(1, 10)
num2 = randint(1, 10)
num3 = randint(1, 10)
num4 = randint(1, 10)
num5 = randint(1, 10)

menor = maior = 0

numeros = (num1, num2, num3, num4, num5)

print(f'Os numeros sorteados foram: ', end='')
for n in numeros:
    print(n, end=' ')

    if menor == 0:
        menor = n
        maior = n
    elif n < menor:
        menor = n
    elif n > maior:
        maior = n

print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
'''

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Os numeros sorteados foram ', end='')
for n in numeros:
    print(n, end=' ')

print(f'\nO maior número sorteado foi {max(numeros)}')
print(f'O menor número sorteado foi {min(numeros)}')
