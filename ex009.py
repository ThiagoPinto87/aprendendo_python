#Escreva um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada.

#Solicita o número a ser feita a tabuada
n1 = int(input('Digite um número inteiro:'))

#Define o tamanho da margem do relatório
margem = 20

#Enunciado com cabeçalho
print('='*margem)
print('A tabuada do {} é:'.format(n1))
print('='*margem)

#Tabuada com margem
print('{} x {:2} = {:2}'.format(n1, 1, n1*1))
print('{} x {:2} = {:2}'.format(n1, 2, n1*2))
print('{} x {:2} = {:2}'.format(n1, 3, n1*3))
print('{} x {:2} = {:2}'.format(n1, 4, n1*4))
print('{} x {:2} = {:2}'.format(n1, 5, n1*5))
print('{} x {:2} = {:2}'.format(n1, 6, n1*6))
print('{} x {:2} = {:2}'.format(n1, 7, n1*7))
print('{} x {:2} = {:2}'.format(n1, 8, n1*8))
print('{} x {:2} = {:2}'.format(n1, 9, n1*9))
print('{} x {:2} = {:2}'.format(n1, 10, n1*10))
print('='*margem)

#Jeito errado que fiz o exercício.
#a = n1 * 1
#b = n1 * 2
#c = n1 * 3
#d = n1 * 4
#e = n1 * 5
#f = n1 * 6
#g = n1 * 7
#h = n1 * 8
#i = n1 * 9
#j = n1 * 10

#print('============================\nSegue abaixo a tabuada do {}:\n============================\n{} x  1 = {}\n{} x  2 = {}\n{} x  3 = {}\n{} x  4 = {}\n{} x  5 = {}'
      #'\n{} x  6 = {}\n{} x  7 = {}\n{} x  8 = {}\n{} x  9 = {}\n{} x 10 = {}\n============================'
      #.format(n1, n1, a, n1, b, n1, c, n1, d, n1, e, n1, f, n1, g, n1, h, n1, i, n1, j))
