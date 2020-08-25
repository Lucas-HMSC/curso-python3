cont18 = homens = mulher20 = 0
while True:
    idade = int(input('Idade = '))
    sexo = input('Sexo [M/F]: ')
    while sexo not in 'MmFf':
        sexo = input('Sexo [M/F]: ')

    if idade > 18:
        cont18 += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1

    esc = input('Deseja continuar [S/N]: ')
    while esc not in 'SsNn':
        esc = input('Deseja continuar [S/N]: ')
    if esc in 'Nn':
        print('Você escolheu sair. Algoritmo encerrado!')
        break

print(f'Total de pessoas com mais de 18 anos: {cont18}')
print(f'Ao todos temos {homens} homens cadastrados.')
print(f'E temos {mulher20} mulher(es) com menos de 20 anos.')
