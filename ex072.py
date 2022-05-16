""" Crie um programa que tenha uma tupla totalmente preechida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso."""

contador = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
            'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

"""pergunta = int(input('Digite um número entre 0 e 20: '))
while pergunta < 0 or pergunta >= len(contador):
    pergunta = int(input('Digite um número: '))"""
while True:
   pergunta = int(input('Digite um número entre 0 e 20: '))
   if 0 <= pergunta <= 20:
       break
   print('Tente novamente.', end='')
print(f'O Número digitado foi o {contador[pergunta]}.')
