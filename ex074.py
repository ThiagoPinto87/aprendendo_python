""" Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla."""

from random import randint

numeros = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)

print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')

print(f'\nO maior número é {max(numeros)}')
print(f'O menor número é {min(numeros)}')




"""# Tente fazer inserindo os dados por input.

dado1 = str(input('Digite o dado1: '))
dado2 = str(input('Digite o dado2: '))
dado3 = str(input('Digite o dado3: '))
dado4 = str(input('Digite o dado4: '))

tupla = dado1 + dado2 + dado3 + dado4

print(tupla.split())"""