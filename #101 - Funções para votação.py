def voto(nasc):
    from datetime import datetime
    ano = datetime.now().year
    idade = (ano - nasc)
    if 16 <= idade <= 18 or idade > 65:
        resp = f'Com {idade} anos: VOTO OPCIONAL.'
    elif idade < 16:
        resp = f'Com {idade} anos: NÃO VOTA.'
    else:
        resp = f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    return resp


print('='*28)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
