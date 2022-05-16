# CONSEGUI SOMENTE COM AJUDA.

# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# ex.: Digite um número: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

# >>>>> Forma string <<<<<
# OBS: Para usar dessa forma o jeito mais correto é fazer por formulas de condição, coisa que ainda iremos aprender.
"""# Captura o número
num = int(input('Digite um número entre 0 e 9999: '))

# Transforma em string
n = str(num)

# Exibe em o relatório
print('Analisando o número {} (Através de string) ...'.format(num))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))"""

# >>>> Forma Matemática <<<<
# Captura o número
num = int(input('Digite um número entre 0 e 9999: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

# Exibe em o relatório
print('Analisando o número {} (Através de string) ...'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))



# >>>> Feito por mim <<<<
"""num = str(input('Digite um número de 0 a 9999: '))

print('Unidade: {}'.format(num[3]))
print('Dezena: {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print('Milhar: {}'.format(num[0]))"""
