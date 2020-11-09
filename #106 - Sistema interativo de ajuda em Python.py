from time import sleep


cor = (
    '\033[m',           # 0 - SEM CORES
    '\033[0;30;41m',    # 1 - VERMELHO
    '\033[0;30;42m',    # 2 - VERDE
    '\033[0;30;43m',    # 3 - AMARELO
    '\033[0;30;44m',    # 4 - AZUL
    '\033[0;30;45m',    # 5 - ROXO
    '\033[7;30m',       # 6 - BRANCO
)


def inicio(txt, c=0):
    tam = len(txt) + 4
    print(cor[c], end='')
    print('=' * tam)
    print(f'  {txt}')
    print('=' * tam)
    print(cor[0], end='')
    sleep(0.5)


def manual(comand):
    inicio(f'Acessando o manual do comando \'{comand}\'', 4)
    print(cor[6], end='')
    help(comand)
    print(cor[0], end='')
    sleep(0.5)


while True:
    inicio('Sistema de Ajuda PyHelp', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        manual(comando)
inicio('Até Logo!', 1)
