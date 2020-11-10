from modulos import moeda_108

num = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda_108.moeda(num)} é {moeda_108.moeda(moeda_108.metade(num))}')
print(f'O dobro de {moeda_108.moeda(num)} é {moeda_108.moeda(moeda_108.dobro(num))}')
print(f'Aumentando 10%, temos {moeda_108.moeda(moeda_108.aumentar(num))}')
print(f'Reduzindo 13%, temos {moeda_108.moeda(moeda_108.diminuir(num))}')
