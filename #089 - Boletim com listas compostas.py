from time import sleep

boletim = []
aluno = []
while True:
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    boletim.append(aluno[:])
    aluno.clear()
    option = str(input('Deseja continuar? [S/N] '))
    while option not in 'SsnN':
        option = str(input('Deseja continuar? [S/N] '))
    if option in 'Nn':
        break
#print(boletim)
sleep(0.5)
print('='*21)
print('{:^21}'.format('BOLETIM'))
print('='*21)
sleep(0.5)
print('{:<4}' .format('Nº'), end='')
print('{:<10}' .format('Nome'), end='')
print('{:^9}'.format('Média'))
print('-'*21)
for num, aluno in enumerate(boletim):
    sleep(0.5)
    print('{:<4}'.format(num), end='')
    print('{:<10}'.format(aluno[0]), end='')
    print('{:^9.1f}'.format((aluno[1] + aluno[2]) / 2))
print('-'*21)
num = 0
while True:
    num = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if num == 999:
        print('Encerrando boletim', end='')
        sleep(0.2)
        print('.', end='')
        sleep(0.2)
        print('.', end='')
        sleep(0.2)
        print('.')
        sleep(0.2)
        print('VOLTE SEMPRE!!!')
        break
    if num <= len(boletim) - 1:
        print(f'Notas de {boletim[num][0]} são {boletim[num][1]} e {boletim[num][2]}')
        print('='*40)
    else:
        print('Opçao incorreta. Digite um número válido de aluno.')
