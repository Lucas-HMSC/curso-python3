from random import randint

print('=*' * 10)
print('Jogo do Par ou Ímpar')
print('=*' * 10)
vitorias = 0
while True:
    PCchoice = randint(0, 10)

    Nchoice = int(input('Escolha um número: '))
    Ochoice = input('P para Par / I para Ímpar: ')

    total = Nchoice + PCchoice

    print('-' * 20)
    print(f'Você jogou {Nchoice} e o computador {PCchoice}. Total é {total} e ', end='')
    if total % 2 != 0:
        print('DEU IMPAR.')
        print('-' * 20)
        if Ochoice in 'Pp':
            print('Você PERDEU!')
            break
        elif Ochoice in 'Ii':
            print('Você VENCEU!')
            vitorias += 1
    else:
        print('DEU PAR.')
        print('-' * 20)
        if Ochoice in 'Pp':
            print('Você VENCEU!')
            vitorias += 1
        elif Ochoice in 'Ii':
            print('Você PERDEU!')
            break
print('=*' * 10)
print(f'Você venceu {vitorias} vezes!')
