from PIL import Image, ImageDraw
#Variaveis globais
dim = 300
img = Image.new('RGB', (dim, dim), "black")
x = 0
r = 100
y = r
offset = 150

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