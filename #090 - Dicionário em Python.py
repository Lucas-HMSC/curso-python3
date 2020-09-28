alunos = {'nome': str(input('Nome: '))}
alunos['media'] = float(input(f'Média de {alunos["nome"]}: '))

print(f'Nome é igual a {alunos["nome"]}')
print(f'Média é igual a {alunos["media"]}')
if alunos['media'] < 5.0:
    print(f'Situação é igual a Reprovado.')
elif alunos['media'] < 7.0:
    print('Situação é igual a Recuperação.')
else:
    print('Situação é igual a Aprovado.')
