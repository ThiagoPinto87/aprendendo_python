""" Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados num dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior
numero no dado."""

# Não consegui ordenar os dicionários. Tive que assistir a resolução do professor guanabara.

"""# Importação de bibliotecas
from random import randint
from time import sleep

# Iterações iniciais e zeradas
tt_jogadas = dict()
resultado = list()
cont = 1

# Simula os jogos dos jogadores imprimindo os resultados
for j in range(4):
    tt_jogadas['nome'] = 'Jogador' + str(cont)
    tt_jogadas['jogo'] = randint(1, 6)
    cont += 1
    resultado.append(tt_jogadas.copy())

print('VALORES SORTEADOS')
for r in resultado:
     print(f'{resultado[r]["nome"]} tirou {resultado[r]["jogo"]} no dado.')
     sleep(1)
resultado.sort()"""

# Importação de bibliotecas.
from random import randint
from time import sleep
from operator import itemgetter

print('-=-=-=- JOGO DE DADOS -=-=-=-')
sleep(2.5)
# Simula o jogo de cada jogador.
jogo = {'Jogador 1': randint(1, 6),  # Cria a key com o nome do jogador e insere um valor aleatório de 1 a 6.
        'Jogador 2': randint(1, 6),  # Cria a key com o nome do jogador e insere um valor aleatório de 1 a 6.
        'Jogador 3': randint(1, 6),  # Cria a key com o nome do jogador e insere um valor aleatório de 1 a 6.
        'Jogador 4': randint(1, 6)}  # Cria a key com o nome do jogador e insere um valor aleatório de 1 a 6.

ranking = list()  # Cria um novo dicionário chamado ranking.

# Imprime o resultado dos jogos
for k, v in jogo.items():  # Laço de repetição buscando cada item do dicionário jogo.
    print(f'O {k} tirou {v} no dado.')  # Imprime cada Key "k" e Valor "v" na f-string criada.
    sleep(1)  # insere um tempo de espera de 1 segundo ao final de cada laço de repetição.

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

sleep(0.5)
print('-=-=-=-=- RANKING -=-=-=-=-=-')
sleep(2)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(0.5)
print('-=' * 14)
