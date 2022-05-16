"""Escreva um programa que leia dois numeros inteiros e compare-os, mostrado na tela uma mensagem:
- O primeiro valor é maior
- o segundo valor é maior
- Não existe valor maior, os dois são iguais."""

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

if num1 > num2:
    print('O primeiro valor é maior.')
elif num1 == num2:
    print('Não existe valor maior, os dois são iguais!')
else:
    print('O segundo valor é maior.')
