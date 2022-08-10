""" Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somarPar(). A primeira
função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os
valores pares sorteados pela função anterior."""

# Importação de bibliotecas
from random import randint

numeros = list()  # podia ser "[]"


def sorteia():
    for numero in range(0, 5):
        numero = randint(0, 9)
        numeros.append(numero)
    print('Sorteando 5 números temos: ', end="")
    for n in numeros:
        print(f'{n} ', end="")
    print('Pronto!')


def soma_par():
    print(f'Somando os valores {numeros}, temos: ', end="")
    soma = cont = 0
    for par in numeros:
        if par % 2 == 0:
            soma += par
            cont += 1
    print(soma)


sorteia()
soma_par()
