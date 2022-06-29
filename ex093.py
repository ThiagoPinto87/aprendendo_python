""" Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato. 3:40"""


aproveitamento = dict()
aproveitamento['nome'] = str(input('Nome do Jogador: ')).strip().upper()
qtd_partidas = int(input(f'Quantidade de partidas que {aproveitamento["nome"]} jogou? '))
gols = list()
for g in range(qtd_partidas):
    gols.append(int(input(f'Quantos gols na partida {g+1}? ')))
aproveitamento['gol_partida'] = gols.copy()
aproveitamento['tt_gols'] = sum(aproveitamento["gol_partida"])

print('-=' * 35)
print(aproveitamento)

print('-=' * 35)
for i, v in aproveitamento.items():
    print(f'O campo {i} tem valor {v}.')

print('-=' * 35)
print(f'O {aproveitamento["nome"]} jogou {qtd_partidas} partidas.')
for g in range(len(aproveitamento['gol_partida'])):
    print(f'=> Na partida {g+1}, fez {aproveitamento["gol_partida"][g]} gols.')
print(f'Foi um total de {aproveitamento["tt_gols"]} gols.')
