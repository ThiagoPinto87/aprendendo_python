# Faça um programa que leia uma frase pelo teclado e mostre:
#  - Quantas vezes aparece a letra "A".
#  - Em que posição ela aparece a primeira vez.
#  - Em que posição ela aparece a ultima vez.


# >>> Forma que resolvi o problema <<<
# Gostei mais da forma do prof. pois já trata a frase no início.

"""
frase = str(input('Digite uma frase: ')).strip()

print('A letra "a" aparece {} vezes.'.format(frase.upper().count('A')))
print('A letra "a" aparece a primeira vez na posição {}!'.format(frase.upper().find('A') + 1))
print('A letra "a" aparece a última vez na posição {}!'.format(frase.upper().rfind('A') + 1))
"""

# >>> Forma que o Prof. Guanabara resolveu <<<

frase = str(input('Digite uma frase: ')).upper().strip()

print('A letra "a" aparece {} vezes.'.format(frase.count('A')))
print('A letra "a" aparece a primeira vez na posição {}!'.format(frase.find('A') + 1))
print('A letra "a" aparece a última vez na posição {}!'.format(frase.rfind('A') + 1))
