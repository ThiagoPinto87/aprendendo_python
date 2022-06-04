"""Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta."""

# Forma que o professor Guanabara fez. Gostei mais dessa forma.

lista = [[], [], []]  # Cria a lista para depois fazer a matriz.
for c in range(3):  # Laço de repetição para fazer o primeiro índice da lista
    for l in range(3):  # Armazena 3 números para cada índice da lista do laço de repetição acima.
        num = int(input(f'Digite valor para [{c}, {l}]: '))  # Captura os números. Na estrutura já informa o índice que será inserido.
        lista[c].append(num)  # Insere a lista de números em cada índice na variável lista.
for x in lista:  # Laço de repetição para que ele imprima cada índice da lista individualmente até terminar a lista.
    print(x)  # Imprime conforme determinado pelo laço.



"""lista = [[], [], []]
for n in range(0, 3):
    num = int(input(f'Digite valor para [0, {n}]: '))
    lista[0].append(num)

for c in range(3):
    con = int(input(f'Digite valor para [1, {c}]: '))
    lista[1].append(con)

for i in range(3):
    ind = int(input(f'Digite valor para [2, {i}]: '))
    lista[2].append(ind)

print('-=' * 15)
for x in lista:
    print(x)"""
