"""Crie um programa que o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela."""

lista = []
ultimo_num = num = 0
for n in range(5):
    num = int(input('Digite um valor: '))
    if n == 0 or num > max(lista):
        lista.append(num)
        print('O número foi inserido no final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'O numero foi inserido na posição {pos}')
                break
            pos += 1
print('-#' * 30)
print(f'Os números digitados foram: {lista}')
