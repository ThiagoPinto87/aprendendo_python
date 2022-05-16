"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o
 valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado."""

"""
>>>COMENTÁRIO<<<
Fiz o exercício de forma praticar as strings de condições. Pois para confeccionar o programa eu o
 faria de forma inversa, calculando à partir da margem do salário e já verificando a possibilidade de parcelas
 com base no juros (o que não foi pedido na atividade).

"""

print('-=' * 35)
print('>' * 18, 'PROGRAMA FINANCIADOR DE IMÓVEIS', '<' * 18)
print('-=' * 35)

# Captura o valor da casa.
vlr_casa = float(input('Digite o valor da casa: R$ '))

# Captura o salário do comprador.
salario = float(input('Digite o valor do salário: R$ '))

# Captura a quantidade de anos quer comprar.
anos = int(input('Em quantos anos quer financiar? '))
qtd_parcelas = anos * 12

# Calcula a margem solicitada.
margem_solicitada = vlr_casa / qtd_parcelas

# Calcula a margem das parcelas do comprador.
print('_' * 68)
margem = salario * (30/100)

# Avalia se com a margem e a quantidade de parcelas, o empréstimo será aprovado ou não.
necessidade_parcelas = vlr_casa / margem

if margem_solicitada <= margem:
    vlr_parcelas = vlr_casa / qtd_parcelas
    print('\33[34mFinanciamento APROVADO!\33[m As parcelas ficarão no valor de R${:.2f}'.format(vlr_parcelas))
else:
    vlr_margem = vlr_casa / margem
    print('\33[33mFinanciamento NEGADO!\33[m, com base na sua margem de R${:.2f},'.format(margem))
    print('você só pode financiar em {:.0f} anos.'.format(necessidade_parcelas/12))