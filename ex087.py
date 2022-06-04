""" Aprimore o desafio anterior, mostrando no final:
a) A soma de todos os valores pares digitados;
b) A soma dos valores da terceira coluna.
c) O Maior valor digitado na segunda linha."""


# VOLTAR PARA A AULA 86 REFAÇA O EXERCÍCIO ATÉ COMPREENDER BEM E DEPOIS VOLTE PARA ESTE.


lista = [[], [], []]  # Cria a lista para depois fazer a matriz.
for c in range(3):  # Laço de repetição para fazer o primeiro índice da lista
    for l in range(3):  # Armazena 3 números para cada índice da lista do laço de repetição acima.
        num = int(input(f'Digite valor para [{c}, {l}]: '))  # Captura os números. Na estrutura já informa o índice que será inserido.
        lista[c].append(num)  # Insere a lista de números em cada índice na variável lista.
print('-=' * 20)
for x in lista:  # Laço de repetição para que ele imprima cada índice da lista individualmente até terminar a lista.
    print(f'{x}')  # Imprime conforme determinado pelo laço com formatação da "f" string.

for x in lista:
    if x % 2 == 0:
        print(x)
