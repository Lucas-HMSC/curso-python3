
print('-'*16)
print('Lista de Compras')
print('-'*16)
soma = mil = menor = 0
menorN = ''
while True:
    nome = input('Nome do produto: ')
    preco = float(input('Preço: R$ '))
    soma += preco
    if preco > 1000:
        mil += 1
    if menor == 0:
        menor = preco
        menorN = nome
    elif preco < menor:
        menor = preco
        menorN = nome
    option = ' '
    while option not in 'SN':
        option = str(input('Continuar? [S/N] ')).strip().upper()[0]
    if option in 'Nn':
        print('Você escolheu sair.')
        print('-'*30)
        break
    while option not in 'Ss':
        print('Opção incorreta.')
        option = input('Continuar? [S/N] ')



print(f'O total da compra foi R$ {soma:.2f}')
print(f'Temos {mil} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {menorN} que custa R$ {menor:.2f}')
