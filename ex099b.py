""" Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""

from time import sleep


def maior(*num):
    cont = maior = 0
    for n in num:
        if cont == 0:
            maior = n
        elif n > maior:
            maior = n
        cont += 1
    print('-=' * 15)
    print('Analisando os números...')
    print(num)
    print(f'Foram gerados {cont} numeros.')
    print(f'O maior número é {maior}')


# Programa principal
maior(5, 2, 3, 4, 7, 1)
maior(1, 3, 9, 4, 6)
maior(0, 1, 4)
maior(9, 6)
maior(2)
maior()
