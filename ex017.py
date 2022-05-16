# Fala um programa que leia o cumprimento do cateto oposto e do cateto adjacente de um triangulo retângulo,
# calcule e mostre o comprimento da hipotenusa.

from math import hypot

# Captura cateto oposto
catopo = float(input('Digite cateto oposto:'))

# Captura cateto adjacente
catadj = float(input(('Digite cateto adjacente:')))

# Chama a função hypot (hipotenusa)
hipotenusa = hypot(catopo, catadj)

# Imprime o resultado do comprimento da hipotenusa
print('O comprimento da hipotenusa desse triângulo retângulo é {:.2f}'.format(hipotenusa))
