#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,27
dinheiro = float(input('Quantos reais tem na carteira? R$'))
conversor = dinheiro / 3.27
print('Você pode comprar US${:.2f}.'.format(conversor))
