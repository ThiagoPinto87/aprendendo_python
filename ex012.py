#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
produto = float(input('Digite o preço do produto: R$'))
novopreco = produto - (produto * 0.05)
print('O novo preço do produto é R${:.2f} com 5% de desconto.'.format(novopreco))
