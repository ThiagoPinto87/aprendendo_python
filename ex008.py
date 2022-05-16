#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
n1 = float(input('Digite uma medida em metros:'))
cent = n1 * 100
mili = n1 * 1000
print('O resultado da medida de {}m é: {:.0f}cm e {:.0f}mm.'.format(n1, cent, mili))
