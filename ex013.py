# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

# Captura o valor do salário.
salario = float(input('Digite o salário: R$'))

# Calculo do novo salário
novosalario = salario + (salario * 0.15)

# printa em tela
print('O novo salário do funcionário passa a ser R${:.2f}.'.format(novosalario))
