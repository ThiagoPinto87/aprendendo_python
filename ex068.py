""" Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou."""

# Importação de bibliotecas.
from random import randint

# Captura a informação inicial se o usuário quer jogar como PAR ou IMPAR.
jogador = int(input("Par ou Ímpar: [1] PAR / [2] IMPAR: "))[0]

# Captura a primeira jogada.
num_jogador = int(input("Digite um número de 0 a 9: "))[0]

# Faz a jogada do computador.
num_computador = int(randint(0, 9))

# Controlador de quantidade de jogadas vitoriosas.
cont = 0

# Calculo da primeira jogada.
calculo = num_jogador + num_computador

# Se o jogador escolheu PAR:
if jogador == 1:
    # Enquanto der PAR (Parte ganhadora).
    while calculo % 2 == 0:
        print(f'{num_jogador} + {num_computador} = {num_jogador + num_computador} é PAR.')
        print('Parabéns você ganhou! Vamos outra...')
        num_jogador = int(input("Digite um número de 0 a 9: "))
        calculo = num_jogador + num_computador
        cont += 1
    # Se der ÍMPAR (Parte perdedora).
    print(f'{num_jogador} + {num_computador} = {num_jogador + num_computador} é \33[31mIMPAR\33[m.')
    print('Você perdeu!')
    print(f'Você ganhou {cont} vez(es) consecutiva(s).')
# Se o jogador escolheu ÍMPAR
elif jogador == 2:
    # Enquanto der IMPAR (Parte vencedora).
    while calculo % 2 != 0:
        print(f'{num_jogador} + {num_computador} = {num_jogador + num_computador} é IMPAR.')
        print('Parabéns você ganhou! Vamos outra...')
        num_jogador = int(input("Digite um número de 0 a 9: "))
        calculo = num_jogador + num_computador
        cont += 1
    # Se der PAR (Parte perdedora).
    print(f'{num_jogador} + {num_computador} = {num_jogador + num_computador} é \33[31mPAR\33[m.')
    print('Você perdeu!')
    print(f'Você ganhou {cont} vez(es) consecutiva(s).')
