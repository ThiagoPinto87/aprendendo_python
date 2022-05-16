# Crie um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex.: Ana Maria de Souza
# Primeiro: Ana
# Último: Souza.


# >>>> Forma que resolvi o problema <<<<
# Gostei mais da forma do prof. Guanabara, pois da forma dele, além de ser visualmente mais simples economiza na memória do pc.

"""
nome = str(input('Digite seu nome completo: ')).strip()
dividido = nome.split()
ultimo = int(len(dividido)-1)

print('Primeiro: {}'.format(dividido[0]))
print('Último: {}'.format(dividido[ultimo]))
"""

# >>>> Forma do prof. Guanabara <<<<

nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()

print('Primeiro: {}'.format(n[0]))
print('Último: {}'.format(n[len(n)-1]))
""" Observe na string acima que o objeto fracionado "n" conta a partir do 0, já o "len" conta a partir do 1, o que ajuda com o problema."""
print(len(n))
