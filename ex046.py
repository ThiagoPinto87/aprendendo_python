"""
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
com pausa de 1 segundo entre eles.
"""

# Importação de bibiotecas
from time import sleep

# Pede para iniciar.
for contagem in range(10, -1, -1):
    print(contagem)
    sleep(1)
print('P A R A B E N S ! ! !')
