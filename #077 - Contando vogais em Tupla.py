palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for palavra in palavras:
    print(f'Na palavra {palavra.upper()} temos ', end='')
    for letra in palavra:
        if letra in 'AaEeIiOoUu':
            print(letra, end=' ')
    print('')
