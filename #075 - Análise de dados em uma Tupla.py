'''
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
num3 = int(input('Digite mais um numero: '))
num4 = int(input('Digite o último numero: '))
'''
numeros = (int(input('Digite um numero: ')),
           int(input('Digite outro numero: ')),
           int(input('Digite mais um numero: ')),
           int(input('Digite o último numero: ')))

print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes.')
if numeros.count(3) == 0:
    print(f'O valor 3 não foi digitado em nenhuma posição.')
else:
    position = numeros.index(3) + 1
    print(f'O valor 3 foi digitado na {position}ª posição.')

print('Os valores pares digitados foram ', end='')
for numero in numeros:
    if numero % 2 == 0:
        print(numero, end=' ')
