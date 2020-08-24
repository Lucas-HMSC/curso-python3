n = soma = cont = 0
while True:
    n = int(input('Digite um número inteiro (999 to exit): '))
    if n == 999:
        print('Você escolheu sair.')
        break
    soma += n
    cont += 1

print(f'Você digitou {cont} número(s) e a soma total é {soma}.')
