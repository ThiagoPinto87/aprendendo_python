""" Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e
comprimento) e mostre o tamanho da área do terreno."""


def area(l, c):
    m2 = l * c
    print(f'A área de um terreno de {l:.2f} x {c:.2f} é de {m2:.2f}m².')

# Programa Principal
print('Controle de Terrenos')
print('---------------------')
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)
