from random import randint

numeros = list()
ctr = 0
while True:
    ctr = randint(0, 11)
    print('Numero gerado:', ctr)
    if ctr not in numeros:
        numeros.append(ctr)
        print('Número adicionado.')
    else:
        print('Número repetido não será adicionado.')
    option = str(input('Deseja continuar? [S/N] '))
    while option.strip().upper() not in 'SN':
        option = str(input('Opção inválida. Deseja continuar? [S/N] '))
    if option.strip().upper() == 'N':
        break
numeros.sort()
print(numeros)
