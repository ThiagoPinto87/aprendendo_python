""" Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""

from time import sleep

def maior(* num):
    cont = maior = 0
    print('-=' * 25)
    print('Analisando os numeros passados...')
    sleep(0.7)
    for n in num:
        print(f'{n} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = n
        elif n > maior:
            maior = n
        cont += 1
    sleep(0.5)
    print(f'\nForam informado {cont} valores ao todo.')
    print(f'O maior valor informado foi o {maior}')


# Programa principal
maior(1, 3, 5, 8, 9, 0)
maior(7, 2, 3, 6)
maior(8, 5)
maior(2)
maior()