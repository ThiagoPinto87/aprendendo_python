# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.

# Importação de bibliotecas

from math import cos, sin, tan, radians

# Captura o ângulo
num = float(input('Digite um ângulo a ser calculado:'))

# Calcula o seno, cosseno e tangente
sen = sin(radians(num))
cos = cos(radians(num))
tan = tan(radians(num))

# Imprime o resultado
print('Os resultados para o angulo {}º são:'.format(num))
print('Seno: {:.2f}'.format(sen))
print('Cosseno: {:.2f}'.format(cos))
print('Tangente: {:.2f}'.format(tan))
