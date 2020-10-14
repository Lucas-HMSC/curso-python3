pessoa = {}
pessoas = []
option = ''
soma = 0
mulheres = []
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('Opção inválida. Digite F ou M.')
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    soma += pessoa['idade']
    if pessoa['sexo'].strip() in 'Ff':
        mulheres.append(pessoa['nome'])
    option = str(input('Deseja continuar? [S/N]'))
    while option not in 'SsNn':
        option = str(input('Deseja continuar? [S/N]'))
    if option.strip() in 'Nn':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'A média de idade foi {soma / len(pessoas):.2f} anos.')
print(f'Dentre as {len(pessoas)} pessoas cadastradas, {len(mulheres)} são mulheres: ', end='')
for n in mulheres:
    print(f'{n}', end=' ')
print(f'\nDentre as {len(pessoas)} cadastradas, essas possuem idade acima da média: ', end='')
for p in pessoas:
    if p['idade'] >= (soma / len(pessoas)):
        print(f'{p["nome"]}', end=' ')
print('\nENCERRADO!!!')
