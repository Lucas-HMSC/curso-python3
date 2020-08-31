preços = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-'*30)
print('{:*^30}'.format('Listagem de Preços'))
print('-'*30)

for position in range(0, len(preços)):
    if position % 2 == 0:
        print('{:.<20}'.format(preços[position]), end='R$ ')
    else:
        print('{:>7.2f}'.format(preços[position]))
