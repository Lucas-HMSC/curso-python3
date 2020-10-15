def area(comp, larg):
    print(f'A área de um terreno {larg:.1f}x{comp} é de {larg * comp}m².')


print(f'{"Controle de Terrenos":^20}')
print('=' * 20)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(larg=largura, comp=comprimento)
