from time import sleep


def maior(* num):
    print('*='*18)
    sleep(0.5)
    print('Analisando os valores passados...')
    sleep(0.5)
    maior = menor = 0
    if len(num) != 0:
        for i, n in enumerate(num):
            if i == 0:
                maior = n
                menor = n
            else:
                if n > maior:
                    maior = n
                elif n < menor:
                    menor = n
            print(n, end=' ')
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior} e o menor foi {menor}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
