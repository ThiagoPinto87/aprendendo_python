""" Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
a) Quantas vezes apareceu o valor 9;
b) Em que posição foi digitado o primeiro valor 3;
c) Quais foram os números pares."""

# Captura os números digitados já os inserindo em tuplas.
num = (int(input('Digite o primeiro valor: ')),
       int(input('Digite o segundo valor: ')),
       int(input('Digite o terceiro valor: ')),
       int(input('Digite o quarto valor: ')), )

# Imprime a tupla digitada.
print(f'Os números digitados foram: {num}')

# Verifica se o número 9 foi digitado.
if 9 in num:
    print(f'\nForam digitados o número "9" {num.count(9)} vezes.')
else:
    print(f'\nO número 9 não foi digitado.')

# Verifica se o número 3 foi digitado.
if 3 in num:
    print(f'O número 3 está no índice {num.index(3)+1}')
else:
    print('O número 3 não foi digitado.')

# Verifica quais foram os números pares digitados.
print('Os números pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(f'{n} ', end='')
