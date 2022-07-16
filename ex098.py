""" Faça um programa que tenha um função chamada contador(), que receba três parâmetros: início, fim e passo e realize
a contagem.
Seu programa tem que realizar três contagens através da função criada
A) De 1 até 10, de 1 em 1;
B) de 10 até 0 de 2 em 2;
C) Uma contagem personalizada."""

# Importação de bibliotecas
from time import sleep


def contador(inic, fim, pas):
    print(f'Contagem de {inic} até {fim} de {pas} em {pas}')
    sleep(2.5)

    if pas < 0:
        pas *= -1
    if pas == 0:
        pas = 1
    if inic < fim:
        contagem = inic
        while contagem <= fim:
            print(f'{contagem}', end=' ')
            contagem += pas
            sleep(0.3)
        print('FIM!')
    else:
        contagem = inic
        while contagem >= fim:
            print(f'{contagem} ', end='')
            contagem -= pas
            sleep(0.3)
        print('FIM!')


# Programa princial
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 25)
print('Agora é sua vez de personalizar a contagem')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
