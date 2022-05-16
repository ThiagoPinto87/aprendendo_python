""" Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (Numero inteiro) e o programa vai informar
quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$50,00, R$20,00, R$10,00, e R$1,00"""

saque = int(input('Qual valor quer sacar? R$ '))
cedulas_50 = saque // 50
cedulas_20 = (saque % 50) // 20
cedulas_10 = ((saque % 50) - (cedulas_20 * 20)) // 10
cedulas_01 = ((saque % 50) - (cedulas_20 * 20) - (cedulas_10 * 10)) // 1
print(f'Sacou {cedulas_50} cédulas de R$50,00')
print(f'Sacou {cedulas_20} cédulas de R$20,00')
print(f'Sacou {cedulas_10} cédulas de R$10,00')
print(f'Sacou {cedulas_01} cédulas de R$1,00')

