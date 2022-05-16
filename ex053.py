'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.'''
'''EX:
APOS A SOPA
A SACADA DA CASA
ANOTARAM A DATA DA MARATONA'''

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
#print('Você digitou a frase: {}'.format(junto))
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('É um palindromo.')
else:
    print('A frase digitada não é um palíndromo.')