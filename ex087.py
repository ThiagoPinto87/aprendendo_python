""" Aprimore o desafio anterior, mostrando no final:
a) A soma de todos os valores pares digitados;
b) A soma dos valores da terceira coluna.
c) O Maior valor digitado na segunda linha."""


matriz_numeros = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Cria a lista para depois fazer a matriz.
par = mai = coluna = 0  # Instancias zeradas e iniciais.
for l in range(3):  # Laço de repetição para preencher os índices da "matriz_numeros".
    for c in range(3):  # Armazena 3 números para cada índice da lista dentro da lista da "matriz_numeros".
        matriz_numeros[l][c] = int(input(f'Digite valor para [{l}, {c}]: '))  # Captura os números. Na estrutura já informa o índice que será inserido.
print('-=' * 20)
for l in range(3):  # Laço de repetição para que ele imprima cada índice da lista individualmente até terminar a lista.
    for c in range(3):
        print(f'[{matriz_numeros[l][c]:^5}]', end='')  # Centralização do texto utilizando 5 caracteres. ":^5"
        if matriz_numeros[l][c] % 2 == 0:  # Verifica se cada valor inserido é par.
            par += matriz_numeros[l][c]  # Insere cada valor verificado como par no laço acima dentro da variável "par"
    print()
print('-=' * 20)
print(f'A soma dos valores par é {par}!')
for l in range(3):  # Laço de repetição de três fases.
    coluna += matriz_numeros[l][2]  # Insere na variável "coluna" cada valor de "matriz_numeros[l][2]" (ou seja
                                    # índice 2 da linha), somando-os.
print(f'A soma da terceira coluna é {coluna}!')  # Imprime o resultado da variável "coluna" acima.

for c in range(3):  # Laço de repetição de três fases.
    if c == 0:  # Verifica se é a primeira informação de "c"
        mai = matriz_numeros[1][c]  # insere a informação de "c" na variável "matriz_numeros[1][c]" (ou seja indice
                                    # 1 da linha.
    elif matriz_numeros[1][c] > mai:  # caso não seja a primeira informação de "c" e for maior que o valor armazenado
                                      # na variável "mai" o valor digitado em matriz_numero[1][c] substituirá a infor-
                                      # mação da variável.
        mai = matriz_numeros[1][c]  # Substitui o valor da variável "mai" em matriz_numeros[1][c]
print(f'O maior valor da segunda linha é {mai}!')  # Imprime o valor da variável "mai".
