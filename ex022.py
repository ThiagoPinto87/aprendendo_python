# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O Nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao todo (em considerar os espaços).
# Quantas letras tem o primeiro nome.

#Captura o nome
nome = str(input('Qual seu nome completo: ')).strip

#Divite o nome em partes
dividido = nome.split()

print('Em maiúscula fica {}'.format(nome.upper()))
print('Em minúscula fica {}'.format(nome.lower()))
print('A quantidade de letas do nome é:', len(nome) - nome.count(' '))
print('O primeiro nome é {} que tem {} letras'.format(dividido[0], len(dividido[0])))
