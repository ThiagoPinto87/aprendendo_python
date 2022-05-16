# Crie um programa que leia o nome de uma pessoa e diga se ela tem ou não com a palavra "SILVA".

# >>> Forma que resolvi o problema <<<
"""
nome = str(input('Qual o nome: ')).strip()

print('SILVA' in nome.upper())
"""

# >>> Forma do prof. Guanabara <<<
nome = str(input('Qual o nome: ')).strip()

print('Tem silva no seu nome? {}'.format('SILVA' in nome.upper()))
