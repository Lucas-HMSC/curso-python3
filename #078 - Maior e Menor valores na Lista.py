from random import randint

lista = []
menor = maior = 0

for i in range(0, 5):
    #lista.append(int(input(f'Digite um número para a Posição {i}: ')))
    lista.append(randint(0, 20))
    if i == 0:
        menor = lista[i]
        maior = lista[i]
    elif lista[i] < menor:
        menor = lista[i]
    elif lista[i] > maior:
        maior = lista[i]

print('=-'*20)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for l in range(0, len(lista)):
    if lista[l] == maior:
        print(f'{l}... ', end='')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for l in range(0, len(lista)):
    if lista[l] == menor:
        print(f'{l}... ', end='')
