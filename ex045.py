"""Crie um programa que faça o computador jogar Jokenpô com você."""

# Cores
vermelho = '\33[31m'
verde = '\33[32m'
amarelo = '\33[33m'
azul = '\33[34m'
fechamento = '\33[m'

# Importação de biblioteca
from random import randint
from time import sleep

# Captura jogada do jogador:
print('{:=^40}'.format(' \33[32mJ O K E N P Ô\33[m '))
print('Pedra: [1]')
print('Papel: [2]')
print('Tesoura: [3]\n')
jogador = int(input('Qual sua jogada? '))

# Captura jogada computador:
computador = randint(1, 3)

if jogador == 1:
    print('Você escolheu {}PEDRA{}!'.format(verde, fechamento))
elif jogador == 2:
    print('Você escolheu {}PAPEL{}!'.format(verde, fechamento))
elif jogador == 3:
    print('Você escolheu {}TESOURA{}!'.format(verde, fechamento))

if computador == 1:
    print('Escolho {}PEDRA{}!'.format(verde, fechamento))
elif computador == 2:
    print('Escolho {}PAPEL{}!'.format(verde, fechamento))
elif computador == 3:
    print('Escolho {}TESOURA{} \n'.format(verde, fechamento))
print('{:^6}'.format('J O'))
sleep(0.5)
print('{:^6}'.format('K E N'))
sleep(0.5)
print('{:^6}'.format('P Ô'))
sleep(0.5)


# Resultado do jogo:
if jogador == computador:
    print('{}Escolhemos a mesma coisa!{}'.format(amarelo, fechamento))
    print('{}IMPATE!!! rsrs... Que legal!{}'.format(amarelo, fechamento))
elif jogador == 1 and computador == 3:
    print ('{}Você ganhou!!!{}'.format(azul, fechamento))
elif jogador == 2 and computador == 1:
    print('{}Você ganhou!!!{}'.format(azul, fechamento))
elif jogador == 3 and computador == 2:
    print('{}Você ganhou!!!{}'.format(azul, fechamento))
elif computador == 1 and jogador == 3:
    print('{}Eu ganhei!!! hahaha!!!{}'.format(amarelo, fechamento))
elif computador == 2 and jogador == 1:
    print('{}Eu ganhei!!! hahaha!!!{}'.format(amarelo, fechamento))
elif computador == 3 and jogador == 2:
    print('{}Eu ganhei!!! hahaha!!!{}'.format(amarelo, fechamento))
else:
    print('{}Jogador: O número {} Não é uma opção válida. Por favor, reinicie o programa.{}'.format(vermelho, jogador, fechamento))

