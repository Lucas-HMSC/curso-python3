def notas(* num, sit = False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    '''
    Forma alternativa:
    turma = {
        'total': len(num),
        'maior': max(num),
        'menor': min(num),
        'media': sum(num) / len(num),
    }
    '''
    total = len(num)
    maior = menor = soma = 0
    for i, n in enumerate(num):
        soma += n
        if i == 0:
            maior = menor = n
        elif n > maior:
            maior = n
        elif n < menor:
            menor = n
    media = soma / total
    turma = {
        'total': total,
        'maior': maior,
        'menor': menor,
        'media': media,
    }
    if sit:
        if media <= 5:
            turma['situação'] = 'RUIM'
        elif media <= 7:
            turma['situação'] = 'RAZOÁVEL'
        else:
            turma['situação'] = 'BOA'
    return turma


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)
