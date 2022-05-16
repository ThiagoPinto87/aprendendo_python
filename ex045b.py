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

# Cabeçalho:
print('{:=^40}'.format(' \33[32mJ O K E N P Ô\33[m '))
print('''Pedra: [0]
Papel: [1]
Tesoura: [2]\n''')

# Captura jogada do computador:
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
jogador = int(input('Qual sua jogada? '))
print('-=' * 12)
print('Computador jogou {}{}{}.'.format(verde, itens[computador], fechamento))
print('Jogador jogou {}{}{}.'.format(verde, itens[jogador],fechamento))
print('-=' * 12)

print('{:^12}'.format('J O'))
sleep(0.5)
print('{:^12}'.format('K E N'))
sleep(0.5)
print('{:^12}'.format('P O'))
sleep(0.3)

# Calcula o vencedor:
if computador == jogador:
    print('Que legal!!! Empatamos')
elif computador == 0: # computador jogou PEDRA.
    if jogador == 1:
        print('{}JOGADOR VENCE!!! PARABÉNS!!!{}'.format(azul, fechamento))
    elif jogador ==2:
        print('{} COMPUTADOR VENCEU!!!'.format(amarelo, fechamento))
elif computador == 1: # computador jogou PAPEL.
    if jogador == 0:
        print('{} COMPUTADOR VENCEU!!!'.format(amarelo, fechamento))
    elif jogador == 2:
        print('{}JOGADOR VENCE!!! PARABÉNS!!!{}'.format(azul, fechamento))
elif computador == 2: # computador jogou TESOURA.
    if jogador == 1:
        print('{} COMPUTADOR VENCEU!!!'.format(amarelo, fechamento))
    elif jogador == 0:
        print('{}JOGADOR VENCE!!! PARABÉNS!!!{}'.format(azul, fechamento))
else:
    print('{}Jogada inválida.{}'.format(vermelho, fechamento))