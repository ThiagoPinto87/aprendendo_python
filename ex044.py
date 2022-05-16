"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
 e condição de pagamento:
- à vista: dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros.
"""

# Captura o valor do produto:
print('/' * 40)
print('{:=^40}'.format(' \33[33mTKF MÓVEIS PLANEJADOS\33[m '))
vlr_produto = float(input('Qual o preço do produto: R$ '))
print('/' * 40)
# Pergunta qual a forma de pagamento:
print('''Escolha sua forma de pagamento?
[1] - À Vista - Dinheiro/Cheque (10% de desconto).
[2] - À Vista - Cartão (5% de desconto).
[3] - Crédito 2x
[4] - Crédito à partir 3x (20% de juros)''')
print('-=' * 20)
print('Qual a forma de pagamento.')
forma_pagamento = (int(input('Forma de pagamento: ')))

# Imprime o relatório:
print('-=' * 20)
print('Valor do produto selecionado: R${:.2f}'.format(vlr_produto))
print('Forma de pagamento:')
if forma_pagamento == 1:
    print('Dinheiro/Cheque: 10% desconto: R${:.2f}'.format(vlr_produto - (vlr_produto * (10/100))))
elif forma_pagamento == 2:
    print('Cartão à vista: 5% desconto: R${:.2f}'.format(vlr_produto - (vlr_produto * (5/100))))
elif forma_pagamento == 3:
    print('Crédito 2x: R${:.2f}'.format(vlr_produto))
elif forma_pagamento == 4:
    tt_parcelas = int(input('Quantas parcelas? '))
    print('Valor total no Crédito: R${:.2f}'.format(vlr_produto + (vlr_produto * (20/100))))
    print('Sua compra parcelada em {}x ficará com parcelas de R${:.2f}'.format(tt_parcelas, ((vlr_produto + (vlr_produto * (20/100))) / tt_parcelas)))
else:
    print('\33[31mInformação inválida. Por favor, reinicie o programa!\33[m')
