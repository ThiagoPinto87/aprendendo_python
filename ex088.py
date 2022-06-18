""" Faça um programa que ajude um jogador da Mega Sena a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta."""

# Importar biblioteca random
from random import randint  # Importa a biblioteca de randomização e seleciona somente a função randomiza inteiros
from time import sleep  # Importa a biblioteca de tempo e seleciona a função sleep (dormir).

# Instancias iniciais, de zeradas ou de contagem:
jogo = list()  # Cria a lista de jogos.
jogadas = []  # Cria a lista que armazena os jogos sorteados.


print('-=' * 17)
print('      SUGESTÃO DA MEGA SENA      ')
print('-=' * 17)
# Criar variável que perguntará qual a quantidade de jogos quer criar
qtdjogadas = int(input('Quantos jogos quer fazer? '))  # Solicita ao usuario a quantidade de jogadas a serem feitas.
tt = 1  # Instância inicial para flag de parada da quantidade de jogadas selecionada pelo usuário.
print('-=' * 4, f'SORTEANDO {qtdjogadas} JOGOS', '-=' * 4)
sleep(2)
while tt <= qtdjogadas:
    # Criar variável que sorteará 6 números
    contador = 0  # Contador  para servir de flag de parada dos 6 números.
    while True:  # Laço de repetição infinita
        num = randint(1, 60)  # Randomiza os números entre 1 e 60.
        if num not in jogo:  # Verifica se o número sorteado já não está na lista (assim não gera números duplicados).
            jogo.append(num)  # Insere o número sorteado na lista jogo.
            contador += 1  # Insere uma contagem para a flag de parada do laço infinito.
        if contador >= 6:  # Faz a flag de parada em 6 números para a lista jogo.
            break  # Aciona a parada quando a verificação acima for satisfeita.
    jogo.sort()  # Organiza em ordem crescente os números sorteados.
    jogadas.append(jogo[:])  # Coloca na lista jogadas o jogo de 6 numeros sorteados.
    tt += 1  # Insere uma contagem para a flag de parada da qtd de jogadas selecionada pelo usuário.
    jogo.clear()  # Limpa os números da lista jogo.
for i, l in enumerate(jogadas):  # Cria laço de repetição para cada jogo dentro da lista jogadas.
    print(f'Jogo {i+1}: {l}')  # Imprime cada jogo ({l}) enumerando-os ({i}).
    sleep(1)
sleep(0.5)
print('-=-=-=-=- Boa sorte!!! -=-=-=-=-=')


# Faz as apostas desejadas pelo usuário

# Imprime o resultado.