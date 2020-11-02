def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


print('='*40)
n = leiaInt('Digite um número: ')
print(f'\033[34mVocê acabou de digitar o número {n}.\033[m')
