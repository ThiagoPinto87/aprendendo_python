""" Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
"""
"""
# Simples
# Captura as informações
inicio = int(input('Digite um valor: '))
fim = int(input('Digite um valor: '))
passo = int(input('Digite um passo: '))

for contador in range(inicio, fim+1, passo):
    print(contador)
print('Fim')"""


# Com um if para confirmar se os números são pares.(condição)
# Captura as informações
inicio = int(input('Digite um valor: '))
fim = int(input('Digite um valor: '))


for contador in range(inicio, fim+1):
        if contador % 2 == 0:
            print(contador, end=' ')
