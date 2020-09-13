#Declaração da matriz passada pelo enunciado
matriz = [
    [1, 1, 1, 12, 12, 12, 2, 2, 2],
    [1, 1, 1, 12, 12, 12, 2, 2, 2],
    [1, 1, 1, 12, 12, 12, 2, 2, 2],
    [13, 13, 13, 3, 3, 3, 14, 14, 14],
    [13, 13, 13, 3, 3, 3, 14, 14, 14],
    [13, 13, 13, 3, 3, 3, 14, 14, 14],
    [4, 4, 4, 15, 15, 15, 5, 5, 5],
    [4, 4, 4, 15, 15, 15, 5, 5, 5],
    [5, 5, 5, 15, 15, 15, 5, 5, 5]
]


def gerarImagem(matriz):
    from PIL import Image, ImageDraw
    dim = 300  # Define a dimensão da imagem a ser gerada
    img = Image.new('RGB', (dim, dim), 'rgb(150, 75, 0)')  # Cria a imagem com as dimensões especificadas e com o background marrom
    draw = ImageDraw.Draw(img)
    cor = 'white'
    #Branco
    #Primeiro Quadrante
    draw.ellipse([(120, 20), (140, 40)], fill=cor, outline=cor, width=1)
    draw.ellipse([(120, 42), (140, 62)], fill=cor, outline=cor, width=1)
    draw.ellipse([(120, 64), (140, 84)], fill=cor, outline=cor, width=1)
    draw.ellipse([(142, 20), (162, 40)], fill=cor, outline=cor, width=1)
    draw.ellipse([(142, 42), (162, 62)], fill=cor, outline=cor, width=1)
    draw.ellipse([(142, 64), (162, 84)], fill=cor, outline=cor, width=1)
    draw.ellipse([(164, 20), (184, 40)], fill=cor, outline=cor, width=1)
    draw.ellipse([(164, 42), (184, 62)], fill=cor, outline=cor, width=1)
    draw.ellipse([(164, 64), (184, 84)], fill=cor, outline=cor, width=1)
    #Segundo Quadrante
    draw.ellipse([(20, 120), (40, 140)], fill=cor, outline=cor, width=1)
    draw.ellipse([(20, 142), (40, 162)], fill=cor, outline=cor, width=1)
    draw.ellipse([(20, 164), (40, 184)], fill=cor, outline=cor, width=1)
    draw.ellipse([(42, 120), (62, 140)], fill=cor, outline=cor, width=1)
    draw.ellipse([(42, 142), (62, 162)], fill=cor, outline=cor, width=1)
    draw.ellipse([(42, 164), (62, 184)], fill=cor, outline=cor, width=1)
    draw.ellipse([(64, 120), (84, 140)], fill=cor, outline=cor, width=1)
    draw.ellipse([(64, 142), (84, 162)], fill=cor, outline=cor, width=1)
    draw.ellipse([(64, 164), (84, 184)], fill=cor, outline=cor, width=1)
    #Terceiro Quadrante
    draw.ellipse([(220, 120), (240, 140)], fill=cor, outline=cor, width=1)
    draw.ellipse([(220, 142), (240, 162)], fill=cor, outline=cor, width=1)
    draw.ellipse([(220, 162), (240, 184)], fill=cor, outline=cor, width=1)
    draw.ellipse([(242, 120), (262, 140)], fill=cor, outline=cor, width=1)
    draw.ellipse([(242, 142), (262, 162)], fill=cor, outline=cor, width=1)
    draw.ellipse([(242, 164), (262, 184)], fill=cor, outline=cor, width=1)
    draw.ellipse([(264, 120), (284, 140)], fill=cor, outline=cor, width=1)
    draw.ellipse([(264, 142), (284, 164)], fill=cor, outline=cor, width=1)
    draw.ellipse([(264, 164), (284, 184)], fill=cor, outline=cor, width=1)
    #Quarto Círculo
    draw.ellipse([(120, 220), (140, 240)], fill=cor, outline=cor, width=1)
    draw.ellipse([(120, 242), (140, 262)], fill=cor, outline=cor, width=1)
    draw.ellipse([(120, 264), (140, 284)], fill=cor, outline=cor, width=1)
    draw.ellipse([(142, 220), (162, 240)], fill=cor, outline=cor, width=1)
    draw.ellipse([(142, 242), (162, 262)], fill=cor, outline=cor, width=1)
    draw.ellipse([(142, 264), (162, 284)], fill=cor, outline=cor, width=1)
    draw.ellipse([(164, 220), (184, 240)], fill=cor, outline=cor, width=1)
    draw.ellipse([(164, 242), (184, 262)], fill=cor, outline=cor, width=1)
    draw.ellipse([(164, 264), (184, 284)], fill=cor, outline=cor, width=1)
    #Preto
    cor = 'black'
    #Primeiro Quadrante
    draw.ellipse([(20, 20), (40, 40)], fill=cor, outline=cor, width=1)
    draw.ellipse([(20, 42), (40, 62)], fill=cor, outline=cor, width=1)
    draw.ellipse([(20, 64), (40, 84)], fill=cor, outline=cor, width=1)
    draw.ellipse([(42, 20), (62, 40)], fill=cor, outline=cor, width=1)
    draw.ellipse([(42, 42), (62, 62)], fill=cor, outline=cor, width=1)
    draw.ellipse([(42, 64), (62, 84)], fill=cor, outline=cor, width=1)
    draw.ellipse([(64, 20), (84, 40)], fill=cor, outline=cor, width=1)
    draw.ellipse([(64, 42), (84, 62)], fill=cor, outline=cor, width=1)
    draw.ellipse([(64, 64), (84, 84)], fill=cor, outline=cor, width=1)
    #Segundo Quadrante
    draw.ellipse([(220, 20), (240, 40)], fill=cor, outline=cor, width=1)
    draw.ellipse([(220, 42), (240, 62)], fill=cor, outline=cor, width=1)
    draw.ellipse([(220, 64), (240, 84)], fill=cor, outline=cor, width=1)
    draw.ellipse([(242, 20), (262, 40)], fill=cor, outline=cor, width=1)
    draw.ellipse([(242, 42), (262, 62)], fill=cor, outline=cor, width=1)
    draw.ellipse([(242, 64), (262, 84)], fill=cor, outline=cor, width=1)
    draw.ellipse([(264, 20), (284, 40)], fill=cor, outline=cor, width=1)
    draw.ellipse([(264, 42), (284, 62)], fill=cor, outline=cor, width=1)
    draw.ellipse([(264, 64), (284, 84)], fill=cor, outline=cor, width=1)
    #Terceiro Quadrante
    draw.ellipse([(120, 120), (140, 140)], fill=cor, outline=cor, width=1)
    draw.ellipse([(120, 142), (140, 162)], fill=cor, outline=cor, width=1)
    draw.ellipse([(120, 164), (140, 184)], fill=cor, outline=cor, width=1)
    draw.ellipse([(142, 120), (162, 140)], fill=cor, outline=cor, width=1)
    draw.ellipse([(142, 142), (162, 162)], fill=cor, outline=cor, width=1)
    draw.ellipse([(142, 164), (162, 184)], fill=cor, outline=cor, width=1)
    draw.ellipse([(164, 120), (184, 140)], fill=cor, outline=cor, width=1)
    draw.ellipse([(164, 142), (184, 162)], fill=cor, outline=cor, width=1)
    draw.ellipse([(164, 164), (184, 184)], fill=cor, outline=cor, width=1)
    #Quarto Quadrante
    draw.ellipse([(20, 220), (40, 240)], fill=cor, outline=cor, width=1)
    draw.ellipse([(20, 242), (40, 262)], fill=cor, outline=cor, width=1)
    draw.ellipse([(20, 264), (40, 284)], fill=cor, outline=cor, width=1)
    draw.ellipse([(42, 220), (62, 240)], fill=cor, outline=cor, width=1)
    draw.ellipse([(42, 242), (62, 262)], fill=cor, outline=cor, width=1)
    draw.ellipse([(42, 264), (62, 284)], fill=cor, outline=cor, width=1)
    draw.ellipse([(64, 220), (84, 240)], fill=cor, outline=cor, width=1)
    draw.ellipse([(64, 242), (84, 262)], fill=cor, outline=cor, width=1)
    draw.ellipse([(64, 264), (84, 284)], fill=cor, outline=cor, width=1)
    #Quinto Quadrante
    draw.ellipse([(220, 220), (240, 240)], fill=cor, outline=cor, width=1)
    draw.ellipse([(220, 242), (240, 262)], fill=cor, outline=cor, width=1)
    draw.ellipse([(220, 264), (240, 284)], fill=cor, outline=cor, width=1)
    draw.ellipse([(242, 220), (262, 240)], fill=cor, outline=cor, width=1)
    draw.ellipse([(242, 242), (262, 262)], fill=cor, outline=cor, width=1)
    draw.ellipse([(242, 264), (262, 284)], fill=cor, outline=cor, width=1)
    draw.ellipse([(264, 220), (284, 240)], fill=cor, outline=cor, width=1)
    draw.ellipse([(264, 242), (284, 262)], fill=cor, outline=cor, width=1)
    draw.ellipse([(264, 264), (284, 284)], fill=cor, outline=cor, width=1)
    img.show()

# Função para binarizar a matriz (15 para branco / 0 para preto)
def limiarização (matriz):
    limiar = 7
    for i, linha in enumerate(matriz):
        for j, numero in enumerate(linha):
            if numero > 7:
                numero = 15
            else:
                numero = 0
            matriz[i][j] = numero


limiarização(matriz)
print(matriz)

option = int(input('Deseja visualizar a representação gráfica? [0 para Não / 1 para Sim]: '))

if option == 0:
    print('Você escolheu sair.')
elif option == 1:
    gerarImagem(matriz)
    print('Imagem gerada.')
