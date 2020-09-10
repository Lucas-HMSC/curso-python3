from PIL import Image, ImageDraw
#Variaveis globais
dim = 300 #Define a dimensão da imagem a ser gerada
img = Image.new('RGB', (dim, dim), "black") #Cria a imagem com as dimensões especificadas e com o background preto
x = 0
r = 100 #Raio do círculo a ser gerado
y = r
offset = 150 #Distanciamento da borda, definido como metade da dimensão para que o circulo gerado esteja centralizado

#Função para desenhar os pixel's
def drawcircle(x, y, offset):
    draw = ImageDraw.Draw(img)
    draw.point((y + offset, x + offset), fill='red')
    draw.point((x + offset, y + offset), fill='red')
    draw.point((-x + offset, y + offset), fill='white')
    draw.point((-y + offset, x + offset), fill='white')
    draw.point((-y + offset, -x + offset), fill='red')
    draw.point((-x + offset, -y + offset), fill='red')
    draw.point((x + offset, -y + offset), fill='white')
    draw.point((y + offset, -x + offset), fill='white')


#Algoritmo de Bresenham
def mindpoint(x, y, offset):
    d = 5 / 4 - r
    drawcircle(x, y, offset)
    while y > x:
        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1
        drawcircle(x, y, offset)


#Chamada da função
mindpoint(x, y, offset)
img.show()