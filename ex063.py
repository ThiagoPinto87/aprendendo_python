""" Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma
Sequencia de Fibonacci."""
""" Fibonacci é a soma do seu atual com o seu antecessor como 0 -> 1 então a proxima sequencia é 2
0 -> 1 -> 1 -> 2, então a proxima sequencia é 3, portanto (.'.)
0 -> 1 -> 1 -> 2 -> 3, entõa a proxima sequencia é 5, e assim sucessivamente."""

# Margens de decoração
print('-' * 30)
print('Sequencia de fibonacci')
print('-' * 30)
# Captura a quantidade de sequencias que o usuário quer ver.
n = int(input('Quantas sequencias você quer ver? '))
# Aglutinador de variáveis zeradas e iniciais.
t1 = 0
t2 = 1
# Imprime a parte inicial da sequencia de fibonacci.
print('~' * 30)
print('{} -> {}'.format(t1, t2), end='')
# Aglutinador de variável inicial.
cont = 3  # Essa variável começa no 3 pois já temos os dois primeiros termos registrados no "t1" e no "t2".
# Laço de repetição com flag de parada com base na quantidade de termos solicitada pelo usuário.
while cont <= n:
    # Formula para calcular o próximo termo de fibonacci.
    t3 = t1 + t2
    # Imprime o próximo termo de fibonacci dentro do laço de repetição.
    print(' -> {}'.format(t3), end='')
    # Transporta os resultados de "t1" para "t2"
    t1 = t2
    # Transporta os resultados de "t2" para "t3"
    t2 = t3
    # Insere um valor a mais na variável de controle de contágem.
    cont +=1
# Finaliza o relatório.
print(' -> FIM')






"""# Importação de Bibliotecas.
from math import floor

# Solicita o número que quer conhecer a sequencia de Fibonacci.
num = int(input('Digite um número: '))
# Solicita quantos termos de Fibonacci o usuário quer ver.
qtd_termos_usuario = int(input('Digite a quantidade de termos: '))

# Aglutinador inicial com 0.
qtd_termos = 0

# Formula do Fibonacci inicial.
fibonacci = num + qtd_termos * 1.61803398875

# Laço de repetição limitado à quantidade determinada pelo usuário.
while qtd_termos < qtd_termos_usuario:
    # Arredondamento do Fibo para demonstração em numeros inteiros.
    floor(fibonacci)
    # Formula do Fibo dentro do laço de repetição acima.
    fibonacci = fibonacci + qtd_termos * 1.61803398875
    # Insere valor de 1 em "qtd_termos".
    qtd_termos += 1
    # Imprime os resultados de fibonacci.
    print('{:.0f}'.format(fibonacci), end=' -> ')
print('Acabou')"""

