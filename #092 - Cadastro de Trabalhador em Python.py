from datetime import datetime
dados = {
    'nome': str(input('Nome: ')),
    'idade': datetime.now().year - int(input('Ano de nascimento: ')),
    'ctps': int(input('Carteira de Trabalho (0 para não tem): '))
}

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = int(input('Salário: R$'))
    dados['aposentadoria'] = (dados['idade'] + 35) - (datetime.now().year - dados['contratação'])
#print(dados)

for i, v in dados.items():
    print(f'{i} tem o valor {v}')
