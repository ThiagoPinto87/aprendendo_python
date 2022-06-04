""" Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente."""

# Criação das listas e variáveis iniciais.
ttnumeros = [[], []]
triagem = 0

# Captura as informações com laço de repetição com flag de parada com quantidade determinada.
for n in range(7):
    triagem = (int(input(f'Digite o {n}º inteiro: ')))
    if triagem % 2 == 0:  # Verifica se o número de triagem é par.
        ttnumeros[0].append(triagem)
    else:
        ttnumeros[1].append(triagem)  # Insere no ttnumeros no índice 1, o número ímpar.
ttnumeros[0].sort()  # Organiza os números pares somente.
ttnumeros[1].sort()  # Organiza os números ímpares somente.

print('-=' * 20)  # Margem decorativa
print(f'Os números pares digitados são: {ttnumeros[0]}')  # Imprime os números pares
print(f'Os números ímpares digitados são: {ttnumeros[1]}')  # Imprime os números ímpares.
