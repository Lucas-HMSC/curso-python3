from random import randint

pessoas = []
dados = []
maior = menor = 0
while True:
    aleat = randint(0,120)
    if aleat < 50:
        break
    else:
        dados.append(str(input('Digite o nome da pessoa: ')))
        dados.append(aleat)
        print(f'Peso: {aleat}')
        pessoas.append(dados[:])
        dados.clear()
        if len(pessoas) == 1:
            maior = menor = aleat
        elif aleat > maior:
            maior = aleat
        elif aleat < menor:
            menor = aleat

print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
