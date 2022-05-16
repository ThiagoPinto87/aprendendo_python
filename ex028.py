# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.


# Pergunta ao usuário se ele acerta.
print('Olá! Sou o computador do Thiago!')
print('Quero brincar de adivinhação com você.')
print('\n')
num_usuário = int(input('Qual o número entre 0 e 5 que estou pensando? '))
print('Você escolheu o número {}'.format(num_usuário))


# Randomiza o número entre 0 e 5
from time import sleep
print('PROCESSANDO...')
sleep(3)
print('\n')
from random import randint
num_escolhido = randint(0, 5)

# Escreve se ganhou ou perdeu.
if num_escolhido == num_usuário:
    print('=' * 25)
    print('Uau!!! Você acertou!!!')
    print('=' * 25)
else:
    print('=' * 38)
    print('Você perdeu!!! Escolhi o número {}!!!'.format(num_escolhido))
    print('=' * 38)
