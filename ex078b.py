""" Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista."""

# SEGUNDA TENTATIVA ERRADA.


lista = []  # Cria uma lista vazia
lista.append(int(input('Digite um valor para a posição 0: ')))  # Solicita valor para o índice 0.
lista.append(int(input('Digite um valor para a posição 1: ')))  # Solicita valor para o índice 1.
lista.append(int(input('Digite um valor para a posição 2: ')))  # Solicita valor para o índice 2.
lista.append(int(input('Digite um valor para a posição 3: ')))  # Solicita valor para o índice 3.
lista.append(int(input('Digite um valor para a posição 4: ')))  # Solicita valor para o índice 4.

print('-' * 40)
print(f'Os valores digitados foram {lista}')
print(f'O maior número digitado é {max(lista)}')
print(f'O menor número digitado é {min(lista)}')



"""for chave, numero in enumerate(lista):
    print(f'O maior número digitado foi o {max(lista)} e foi digitado na posição {max(lista.index(numero))}')"""
