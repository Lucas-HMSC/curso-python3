def fatorial(n=1, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: número a ser calculado.
    :param show: (opcional) Mostra ou não o calculo.
    :return: O valor do fatorial de um número n
    """
    f = 1
    if show:
        for i in range(n, 0, -1):
            f *= i
            if i != 1:
                print(f'{i} x', end=' ')
            else:
                print(f'{i} = {f}')
    else:
        for i in range(n, 0, -1):
            f *= i
        print(f)


num = int(input('Digite um número: '))
opt = str(input('Deseja que seja exibido o cálculo: [S/N]: '))
while opt not in 'SNsn':
    opt = str(input('Opção inválida. Deseja que seja exibido o cálculo: [S/N]: '))
if opt in 'Ss':
    show = True
    fatorial(num, show)
else:
    fatorial(num)
help(fatorial)
