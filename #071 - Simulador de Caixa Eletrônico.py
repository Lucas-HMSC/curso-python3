print('*'*20)
print(' '*3 + 'Banco do Luska' + ' '*3)
print('*'*20)

valor = int(input('Que valor você quer retirar? R$ '))

parc50 = valor // 50
valor -= parc50 * 50
parc20 = valor // 20
valor -= parc20 * 20
parc10 = valor // 10
valor -= parc10 * 10
parc1 = valor

print(f'Total de {parc50:2} cédulas de R$ 50')
print(f'Total de {parc20:2} cédulas de R$ 20')
print(f'Total de {parc10:2} cédulas de R$ 10')
print(f'Total de {parc1:2} cédulas de R$ 1')
