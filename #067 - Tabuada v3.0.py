from time import sleep
n = 0

while True:
    n = int(input('Deseja ver a tabuada de qual número? '))
    if n < 0:
        print('Você escolheu sair. Encerrando algoritmo', end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.2)
        print(' Finalizado!')
        break
    print('='*20)
    for i in range(1, 11):
        print(f'{i:2} x {n:2} = {n * i}')
    print('=' * 20)
