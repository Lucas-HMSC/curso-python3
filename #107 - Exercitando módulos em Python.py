from modulos import moeda_107

num = float(input('Digite o preço: R$ '))
print(f'A metade de {num} é {moeda_107.metade(num)}')
print(f'O dobro de {num} é {moeda_107.dobro(num)}')
print(f'Aumentando 10%, temos {moeda_107.aumentar(num, 10)}')
print(f'Reduzindo 13%, temos {moeda_107.diminuir(num, 13)}')
