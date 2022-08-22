"""Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador
e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente"""


def jogador(nome_jogador='<desconhecido>', num_gols=0):
    """
    Recebe informações de um jogador e coloca em uma "ficha".
    :param nome_jogador: Nome do Jogador.
    :param num_gols: Quantidade de gols (int).
    :return: A "Ficha" do jogador contendo nome e número de gols.
    """
    if not nome_jogador:
        nome_jogador = '<desconhecido>'
    if not num_gols:
        num_gols = 0

    print(f'O jogador {nome_jogador} fez {num_gols} gols.')


# Programa Principal
nome = str(input('Nome do Jogador: ')).strip().upper()
gols = str(input('Quantos gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
jogador(nome, gols)  # Não entendi o porque o professor Guanabara não precisou chamar a função denominada por ele de
# "ficha()". No meu caso precisei chamar ao final do programa principal.
