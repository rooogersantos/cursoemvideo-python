# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
# do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Chapecoense.

brasileirao = ('Palmeiras', 'Flamengo', 'Fluminense', 'Athletico - PR', 'Bragantino',
               'Bahia', 'Coritiba', 'São Paulo', 'Atlético - MG', 'Corinthians',
               'Cruzeiro', 'Botafogo', 'EC Vitória', 'Internacional', 'Santos',
               'Grêmio', 'Vasco da Gama', 'Remo', 'Mirassol', 'Chapecoense')

print('=-' * 90)
print(f'Os primeiro cinco colocados são: {brasileirao[:5]}')
print('=-' * 90)
print(f'Os últimos quatro colocados são: {brasileirao[-4:]}')
print('=-' * 90)
print(f'Times em ordem alfabética: {sorted(brasileirao)}')
print('=-' * 90)
print(f'A Chapecoense está em {brasileirao.index('Chapecoense') + 1}º na classificação geral')
print('=-' * 90)