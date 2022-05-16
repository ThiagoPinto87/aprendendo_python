""" Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista."""

lista = []  # Cria uma lista simples vazia.

# Aglutinador de valores zerados
maior = menor = 0

# Laço de repetição para entrada com 5 valores inserindo as informações na lista vazia.
for n in range(5):
    lista.append(int(input(f'Digite um valor para a posição {n}: ')))  # O "n" imprime cada posição no índice.
    if n == 0:  # Se o "n" for o primeiro resultado do índice, então o primeiro resultado será maior e menor.
        maior = lista[n]  # Colocar o "[n]" ao final da lista para referenciar ao número da vez digitado.
        menor = lista[n]
    elif lista[n] > maior:  # Se o número digitado da vez é maior que o número maior acima.
        maior = lista[n]
    elif lista[n] < menor:  # Se o número digitado da vez é menor que o número menor acima.
        menor = lista[n]

print('-' * 40)
print(f'Os valores digitados foram {lista}')  # Imprime os números digitados conforme sua ordem.
print(f'O maior número digitado foi {maior} nas posições', end=': ')  # Imprime o maior número.
for chave, num in enumerate(lista):  # Laço de repetição com enumerate para verificar a posição do num digitado...
    # ...quando for o maior.
    if num == maior:  # Se o "num" da vez for igual ao maior acima, imprima a chave abaixo.
        print(f'{chave} - ', end='')  # Imprime a chave quando o número for maior informando seu índice.

print()  # Somente para ir para linha abaixo.

print(f'O menor número digitado é {menor}', end=': ')  # Imprime o menor número.
for chave, num in enumerate(lista):  # Laço de repetição com enumerate para verificar a posição do num digitado...
    # ...quando for o menor.
    if num == menor:  # Se o "num" da vez for igual ao menor acima, imprima a chave abaixo.
        print(f'{chave} - ', end='')  # Imprime a chave quando o número for menor informando seu índice.
