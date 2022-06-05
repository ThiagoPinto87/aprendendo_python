""" Aprimore o desafio anterior, mostrando no final:
a) A soma de todos os valores pares digitados;
b) A soma dos valores da terceira coluna.
c) O Maior valor digitado na segunda linha."""


matriz_numeros = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Cria a lista para depois fazer a matriz.
for l in range(3):  # Laço de repetição para preencher os índices da "matriz_numeros".
    for c in range(3):  # Armazena 3 números para cada índice da lista dentro da lista da "matriz_numeros".
        matriz_numeros[l][c] = int(input(f'Digite valor para [{l}, {c}]: '))  # Captura os números. Na estrutura já informa o índice que será inserido.
print('-=' * 20)
for l in range(3):  # Laço de repetição para que ele imprima cada índice da lista individualmente até terminar a lista.
    for c in range(3):
        print(f'[{matriz_numeros[l][c]:^5}]', end='')  # Centralização do texto utilizando 5 caracteres. ":^5"
    print()
print('-=' * 20)
