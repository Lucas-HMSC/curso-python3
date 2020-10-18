from time import sleep


def contador(inicio, fim, passo):
    print('=*' * 20)
    sleep(0.5)
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo *= -1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    ctr = inicio
    if inicio < fim:
        while ctr <= fim:
            sleep(0.5)
            print(ctr, end=' ')
            ctr += passo
        sleep(0.5)
        print('FIM!')
    elif fim < inicio:
        while ctr >= fim:
            sleep(0.5)
            print(ctr, end=' ')
            ctr -= passo
        sleep(0.5)
        print('FIM!')
    sleep(0.5)


contador(1, 10, 1)
contador(10, 0, 2)
print('=*' * 20)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input(f'{"Início: ":<7}'))
fim = int(input(f'{"Fim: ":<7}'))
passo = int(input(f'{"Passo: ":<7}'))
contador(inicio, fim, passo)
