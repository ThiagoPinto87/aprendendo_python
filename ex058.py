''' Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final, quantos palpites foram necessários para vencer.'''

# Cabeçalho interativo.
print('Olá! Sou o computador do Thiago!')
print('Quero brincar de adivinhação com você.\n')

# Pergunta ao usuário se ele acerta.
num_usuário = int(input('Qual o número entre 0 e 10 que estou pensando? '))
print('Você escolheu o número {}'.format(num_usuário))

# Randomiza o número entre 0 e 5
from time import sleep
print('PROCESSANDO...')
sleep(0.5)
from random import randint
num_escolhido = randint(0, 10)

# Aglutinador de variáveis zeradas e iniciais
tentativas = 1
acertou = False

# Escreve se ganhou ou perdeu.
while not acertou:
    num_usuário = int(input('\33[31mVocê errou!\33[m Tente novamente. Digite outro número: '))
    tentativas += 1
    if num_escolhido == num_usuário:
        acertou = True

# Imprime o relatório.
if tentativas <= 5:
    print('=' * 32)
    print('\33[33mUau!!! Você acertou!!!\33[m')
    print('E só precisou de {} tentativas.'.format(tentativas))
    print('=' * 32)
elif tentativas > 5:
    print('=' * 32)
    print('\33[33mVocê ganhou!!!\33[m')
    print('E precisou de {} tentativas. Quase ganhei!!!'.format(tentativas))
    print('=' * 32)

"""# Minha forma de resolver o problema.
# Gostei mais do professor Guanabara, alem da strig ter ficado melhor, o programa ficou mais fácil de entender.
# Pergunta ao usuário se ele acerta.
print('Olá! Sou o computador do Thiago!')
print('Quero brincar de adivinhação com você.\n')
num_usuário = int(input('Qual o número entre 0 e 10 que estou pensando? '))
print('Você escolheu o número {}'.format(num_usuário))


# Randomiza o número entre 0 e 5
from time import sleep
print('PROCESSANDO...')
sleep(0.5)
from random import randint
num_escolhido = randint(0, 10)

# Escreve se ganhou ou perdeu.
tentativas = 1
while num_escolhido != num_usuário:
    num_usuário = int(input('\33[31mVocê errou!\33[m Tente novamente. Digite outro número: '))
    tentativas += 1
if tentativas <= 5:
    print('=' * 32)
    print('\33[33mUau!!! Você acertou!!!\33[m')
    print('E só precisou de {} tentativas.'.format(tentativas))
    print('=' * 32)
elif tentativas > 5:
    print('=' * 32)
    print('\33[33mVocê ganhou!!!\33[m')
    print('E precisou de {} tentativas. Quase ganhei!!!'.format(tentativas))
    print('=' * 32)"""
