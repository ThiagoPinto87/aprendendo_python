""" Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou."""

# Importação de Bibliotecas:
from random import randint

# Foi uma escolha minha não ficar perguntando se o usuário quer par ou impar!

usuário = str(input('Par ou impar? [P/I]: ')).upper().strip()[0]
while usuário not in 'PI':
    usuário = str(input('Par ou impar? [P/I]: ')).upper().strip()[0]
if usuário == 'P':
    escolha = 0
else:
    escolha = 1

cont_vitórias = 0

while True:
    print('-' * 30)
    jogada = int(input("Digite um valor: [0~9] "))
    computador = randint(0, 9)
    calculo = (jogada + computador) % 2
    if calculo == escolha:
        print(f'{jogada} + {computador} = {jogada + computador} ', end='')
        print('DEU PAR' if calculo == 0 else 'DEU IMPAR')  # Conhecido como operador ternário.
        print('Você ganhou! Parabéns')
        cont_vitórias += 1
    else:
        break
print('#' * 30)
print('PERDEU!!!')
print(f'{jogada} + {computador} = {jogada + computador} ', end='')
print('DEU PAR' if calculo == 0 else 'DEU IMPAR')  # Conhecido como operador ternário.
print(f'Você venceu {cont_vitórias} vez(es).')
print('#' * 30)