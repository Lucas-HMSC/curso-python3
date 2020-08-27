numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    numero = int(input('Digite um numero entre 0 e 20: '))
    if numero < 0 or numero > (len(numeros) - 1):
        numero = int(input('Opção inválida. Digite APENAS numeros entre 0 e 20: '))
        print(f'Você digitou o numero {numeros[numero]}.')
        break
    else:
        print(f'Você digitou o numero {numeros[numero]}.')
        break
