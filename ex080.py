"""Crie um programa que o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela."""

# Não consegui fazer, precisei olhar a resposta do exercício.

lista = []
ultimo_num = num = 0
for n in range(5):
    num = int(input('Digite um valor: '))
    if n == 0:
        lista.append(num)
    else:
        for valor in lista:
            if num < min(lista):
                lista.insert(0, num)
                ultimo_num = num
            elif num > max(lista):
                lista.append(num)
                ultimo_num = num
            elif num < ultimo_num:
                lista.insert(lista.index(ultimo_num), num)
                ultimo_num = num
            elif num > ultimo_num:
                lista.insert(lista.index(ultimo_num)+1, num)
                ultimo_num = num
    print(f'O número {num} foi inserino na posição {lista.index(num)}')

print(lista)
