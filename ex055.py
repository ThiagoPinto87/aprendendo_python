""" Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos."""

# Aglutina a informação inicial para contagem setando número 0
maior = 0
menor = 0
# Faz o laço de 5 resultados
for pessoa in range(1, 6):
    # Captura os dados e salva na variável "peso".
    peso = float(input('Digite o peso da {}ª pessoa em kg: '.format(pessoa)))
    # Verifica qual o primeiro registro do laço "pessoa" e atualiza (substitui) os resultados nas variáveis "maior" (lin 4) e "menor" (lin 5).
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        # Verifica os demais resultados do laço "pessoa" que armazena informações na variável "peso" e compara.
        if peso > maior:
            maior = peso  # Se o "peso" foi maior que o resultado da variável "maior", então substitui pelo novo peso lido.
        elif peso < menor:
            menor = peso
print('O maior peso lido foi {}Kg'.format(maior))
print('O menor peso lido foi {}Kg'.format(menor))
