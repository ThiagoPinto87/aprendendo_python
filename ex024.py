# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

# >>> Forma que resolvi o problema <<<
# >>> Gostei mais do meu jeito pois nele eu não me limito a uma palavra com um número finito de letras (desde que cadastrada)

"""
cidade = str(input('Digite o nome da cidade: ')).strip()
dividido = cidade.split()
print('SANTO' in dividido[0].upper())
"""

# >>> Forma de resolver do prof. Guanabara <<<

cid = str(input('Digite o nome da cidade: ')).strip()
print(cid[:5].upper() == 'SANTO')
