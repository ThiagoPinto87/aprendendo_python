# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou íMPAR.

# Forma do prof. Guanabara.
num = int(input('Digite um número: '))
calculo = num % 2
if calculo == 0:
    print('O número {} é PAR.'.format(num))
else:
    print('O numero {} é IMPAR.'.format(num))



# Forma que utilizei para resolver o problema
#Gostei mais da forma do prof. Guanabara que foi ÓBVIO e objetivo.
"""
# Cadastra lista de números ÍMPARES
impar = [1, 3, 5, 7, 9]

# Captura o número
num = int(input('Digite um número: '))

# Calcula a unidade do número.
calculo = num // 1 % 10

# Imprime relatório
if calculo in impar:
    print('O número {} é ÍMPAR!'.format(num))
else:
    print('O número {} é PAR!'.format(num))"""
