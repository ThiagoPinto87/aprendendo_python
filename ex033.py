# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

# Forma do prof. Guanabara

a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
c = float(input('Digite o terceiro número: '))

# Verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

# Imprime relatório
print('O menor valor digitado foi {}.'.format(menor))
print('O maior valor digitado foi {}.'.format(maior))



"""
# Forma que encontrei para resolver o problema
# Apesar de ter gostado mais do meu jeito, nele, eu não pratiquei o IF e ELSE.
# Captura 3 numeros.
num_1 = float(input('Digite o primeiro número: '))
num_2 = float(input('Digite o segundo número: '))
num_3 = float(input('Digite o terceiro número: '))

# Cria uma lista com os 3 números.
print('<>' * 20)
lista = ([num_1, num_2, num_3])
print('Você digitou os seguintes números:')
print(lista)
print('Entre eles:\n')

# Compara qual é o maior.
print('O maior número da lista acima é: ', max(lista))

# Compara qual é o menor.
print('O menor número da lista acima é: ', min(lista))"""
