""" Aprimore o Desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
do aproveitamento de cada jogador."""

time = list()
while True:
    aproveitamento = dict()
    aproveitamento['nome'] = str(input('Nome do Jogador: ')).strip().upper()
    qtd_partidas = int(input(f'Quantidade de partidas que {aproveitamento["nome"]} jogou? '))
    gols = list()
    for g in range(qtd_partidas):
        gols.append(int(input(f'Quantos gols na partida {g+1}? ')))
    aproveitamento['gol_partida'] = gols.copy()
    aproveitamento['tt_gols'] = sum(aproveitamento["gol_partida"])
    time.append(aproveitamento)
    resposta = str(input('Quer continuar? [S/N]? ')).strip().upper()[0]
    if resposta == 'N':
        break

print('-=' * 25)
print('Cod. Nome            Gols           Total')
print('-' * 42)
for c, j in enumerate(time):
    print(f'{c+1:^4} {j["nome"]:15} {str(j["gol_partida"]):<15} {j["tt_gols"]:>3}')  # Para dar certo a organização...
    # ...da tabela, precisei  transformar os gols por partidas em string usando a expressão str.
print('-' * 42)
detalhe_jogador = int(input('Mostrar dados de qual jogador? [999 para encerrar]: '))
while detalhe_jogador != 999:
    if detalhe_jogador-1 >= len(time):
        print(f'Erro, não tem jogador cadastado com código {detalhe_jogador}')
        detalhe_jogador = int(input('Mostrar dados de qual jogador? [999 para encerrar]: '))
    else:
        print(f'- LEVANTAMENTO JOGADOR(A) {time[detalhe_jogador-1]["nome"]}:')
        for a, g in enumerate(time[detalhe_jogador-1]['gol_partida']):
            print(f'No jogo {a+1} fez {g} gols.')
        print('-' * 42)
        detalhe_jogador = int(input('Mostrar dados de qual jogador? [999 para encerrar]: '))
"""while True:
    if detalhe_jogador == 999:
        break
    elif detalhe_jogador-1 >= len(time):
        print(f'Erro, existe jogador cadastado com código {detalhe_jogador}!')
        detalhe_jogador = int(input('Mostrar dados de qual jogador? [999 para encerrar]: '))
    else:
        print(f'- LEVANTAMENTO JOGADOR(A) {time[detalhe_jogador-1]["nome"]}:')
        for a, g in enumerate(time[detalhe_jogador-1]['gol_partida']):
            print(f'No jogo {a + 1} fez {g} gols.')
        print('-' * 42)
        detalhe_jogador = int(input('Mostrar dados de qual jogador? [999 para encerrar]: '))"""
print('<< ENCERRADO >>')



