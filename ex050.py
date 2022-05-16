""" Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for impar, desconsidere-o."""

soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}º número: '.format(c)))
    if n % 2 == 0:
        soma += + n
        cont += 1
    else:
        pass  # O objeto "pass", deixa passar a informação que desejarmos, ela não executa a função e não retorna nada.
print('Você informou {} números pares, que digitados, somam {}.'.format(cont, soma))
