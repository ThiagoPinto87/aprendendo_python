""" Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final mostre:
a) Qual é o total gasto na compra.
b) Quantos produtos custam mais de R$1.000,00
c) Qual é o nome do produto mais barato."""

# Aglutinador de variáveis zeradas e/ou iniciais.
soma = cont_produtos = cont_produtos_1000 = menor_preco = 0
mais_barato = 'A definir'

# Laço de repetição infinito (necessário break).
while True:
    descricao = str(input('Nome do produto: ')).upper().strip()
    preco = float(input('Valor do produto: R$'))
    resposta = ' '  # str(input('Quer continuar a lançar? [S/N]: ')).upper().strip()[0]
    while resposta not in 'SN':
        resposta = str(input('Quer continuar a lançar? [S/N]: ')).upper().strip()[0]
    soma += preco
    cont_produtos += 1
    if preco > 1000:
        cont_produtos_1000 += 1
    if cont_produtos == 1:
        mais_barato = descricao
        menor_preco = preco
    elif preco < menor_preco:
        mais_barato = descricao
    if resposta == 'N':
        break
print('-=' * 25)
print(f'O valor da compra é: R${soma:.2f}')
print(f'{cont_produtos_1000} produtos custaram mais de R$1.000,00')
print(f'O produto mais barato foi {mais_barato} que custa R${menor_preco:.2f}')
