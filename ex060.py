""" Faça um programa que leia um número qualquer e mostre o seu fatorial."""

# Formas do professor Guanabara.

n = int(input('Digite um número para achar seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c  # Ou podemos escrever "f *= c
    c -= 1
print('{}'.format(f))


"""# Com importação de bibliotecas
from math import factorial
n = int(input('Digite um número para achar seu fatorial: '))
f = factorial(n)
print('O fatorial de {}! é {}.'.format(n, f))"""


# Forma que encontrei para resolver o problema.
"""num_inicial = int(input('Digite um número: '))
num = num_inicial - 1
fatorial = num_inicial * num
if num_inicial == 0 or num_inicial == 1:
    fatorial = 1
elif num_inicial < 0:
    print('\33[31mNão existe fatorial para números negativos.\33[m')
    num_inicial = int(input('Digite um número: '))
while num >= 2:
    num -= 1
    fatorial = fatorial * num
print('O {}! corresponde a {}.'.format(num_inicial, fatorial))
"""