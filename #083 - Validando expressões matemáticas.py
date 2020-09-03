expressao = list()
contA = contB = 0
conta = False
expressao.append(input('Digite uma expressão matemática: '))
for letra in expressao:
    for l in letra:
        if l in '+-*/':
            conta = True
        elif l in '(':
            contA += 1
        elif l in ')':
            contB += 1

if contA == contB and conta:
    print('A expressão é válida.')
else:
    print('A expressão não é válida.')
