"""Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""

# Captura o número inteiro
num = int(input('Digite um número: '))

cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        cont += 1
    else:
        print('\033[m', end='')
    print('{} '.format(c), end='')
print('\n \033[mO número {}, foi divisível {} vezes.'.format(num, cont))
if cont == 2:
    print('Por isso ele é primo!')
else:
    print('Por isso ele \033[31mnão é primo!')

