""" Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem
de colocação. Depois mostre:
a) Apenas os 5 Primeiros colocados.
b) Os últimos 4 colocados da tabela.
c) Uma lista com os times em ordem alfabética.
d) Em que posição na tabela está o time do Palmeiras."""

times = 'Corinthians', 'Bragantino', 'Atlético-MG', 'Coritiba', 'São Paulo', 'Santos', 'Cuiabá', 'Internacional', 'Avaí',\
        'América-MG', 'Palmeiras', 'Flamengo', 'Botafogo', 'Fluminense', 'Ceará', 'Athletico', 'Atlético-GO','Goiás', \
        'Juventude', 'Fortaleza'
print(f'Os cinco primeiros colocados são {times[:5]}')
print(f'Os últimos 4 colocados são {times[-4:]}')
print(f'Os times em ordem alfabética: {sorted(times)}')
print(f'O Palmeiras está em {times.index("Palmeiras")}º colocado.')
