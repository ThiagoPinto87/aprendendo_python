# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#   - Para salários superiores a R$1.250,00, calcule um aumento de 10%.
#   - Para salários inferiores ou iguais, o aumento é de 15%.


# O prof. Guanabara utilizou o objeto "novo" uma única vez igual ao exercício da passagem pela distancia.
# Captura o salário do funcionário.
print('><' * 20)
sal_atual = float(input('Digite o salário do funcionário: R$'))
print('Você digitou o salário de R${:.2f}'.format(sal_atual))

# Calcula o salário do funcionário.

if sal_atual > 1250:
    sal_novo_10 = sal_atual + (sal_atual * 10/100)
    print('Seu salário sofrerá um majoramento de 10%. Portanto, seu salário passa a ser de R${:.2f}'.format(sal_novo_10))
else:
    saL_novo_15 = sal_atual + (sal_atual * 15/100)
    print('Seu salário sofrerá um majoramento de 15%. Portanto, seu salário passa a ser de R${:.2f}'.format(saL_novo_15))
