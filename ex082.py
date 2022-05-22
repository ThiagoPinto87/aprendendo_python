""" Crie um programa que leia vários números e coloque-os em uma lista.
Depois crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas."""

numeros = []
resp = 'S'
while True:
    numeros.append(int(input('Digite um número: ')))
    resp = input('Quer continuar? [S/N]: ').strip().upper()
    if resp == 'N':
        break
pares = []
impares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'Os números digitados foram: {numeros}')
print(f'Pares digitados: {pares}')
print(f'Impares digitados: {impares}')
