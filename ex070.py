""" Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai contunuar.
No final mostre:
a) Qual é o total gasto na compra.
b) Quantos produtos custam mais de R$1.000,00
c) Qual é o nome do produto mais barato."""

# NEM TESTEI O PROGRAMA, TEMOS QUE VER SE DEU CERTO.

# Margem decorativa com cabeçalho.
print('=-' * 20)
print(' ' * 10, 'SKILO TECNOLOG', ' ' * 10)
print('=-' * 20)

# Aglutinador de variáveis zeradas e iniciais.
soma = 0
produto_1000 = 0
produto_barato = ''
produto = None
pergunta = 'N'

# Primeira solicitação de input de valores.
produto = str(input('Descrição do produto: '))
valor = float(input('Valor do produto: R$'))
soma += valor
if valor > 1000:
    produto_1000 += 1
if valor < valor:
    produto_barato = produto

while True:
    pergunta = str(input('Quer continuar a lançar? [S/N]: ')).strip().upper()[0]
    if pergunta == 'S':
        # Solicita o produto e seu valor.
        produto = str(input('Descrição do produto: '))
        valor = float(input('Valor do produto: R$'))
        soma += valor
        if valor > 1000:
            produto_1000 +=1
        if valor < valor:
            produto_barato = produto
    print(f'A soma dos produtos é {soma}')
    print(f'Tiveram {produto_1000} menores que R$1.000,00')
    print(f'O produto mais barato é {produto_barato}')


