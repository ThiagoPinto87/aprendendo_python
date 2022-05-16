# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Exemplo: Digite um número:6.127, O número 6.127 tema aparte inteira 6.

'''# Importação de bibliotecas
from math import trunc

# Captura o número real.
num = float(input('Digite um número real:'))

# Imprime o resultado.
print('O número {} tem a parte inteira {}'.format(num, trunc(num)))'''

# Outra forma de resolver o problema.

# Captura o número real.
num = float(input('Digite um número real:'))

# Imprime o resultado.
print('O número {} tem a parte inteira {}'.format(num, int(num)))