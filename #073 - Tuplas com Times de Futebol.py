campBR = ('Flamengo', 'Atlético-MG', 'Botafogo', 'Bahia', 'Palmeiras', 'Vasco', 'Santos', 'Bragantino', 'Corinthians',
          'Atlético-GO', 'Grêmio', 'Fluminense', 'Sport', 'Ceará', 'Coritiba', 'Internacional', 'Fortaleza',
          'Athletico', 'Goiás', 'São Paulo')

print(campBR)
print(f'Os 5 primeiros colocados são: {campBR[:5]}')
print(f'Os 4 últimos são: {campBR[-4:]}')
print(f'Times em ordem alfabética: {sorted(campBR)}')
position = campBR.index('São Paulo') + 1
print(f'O São Paulo está na {position}ª posição')
