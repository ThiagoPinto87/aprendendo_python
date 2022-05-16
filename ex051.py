"""Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritimética (PA).
No final, mostre os 10 primeiros termos dessa progressão."""

# termo = 5
# razao = 2


prim_termo = int(input('Digite o primeiro número do termo: '))
razao = int(input('Digite a razão: '))
qtd_termos = int(input('Qual a quantidade de termos? '))
for c in range(prim_termo, prim_termo + qtd_termos * razao, razao):
    print('{} '.format(c), end='-> ')
print('ACABOU')

# Razão quer dizer um número menos o outro (x - y)
