""" Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo."""

while True:
    num = int(input('Você quer ver a tabuada de qual valor? '))
    numerador = 0
    if num < 0:
        break
    for numerador in range(1, 11):
        print(f'{num} x {numerador:2} = {num * numerador}')
    """while numerador <= 10:
        mult = num * numerador
        print(f'{num} x {numerador:2} = {mult}')
        numerador += 1"""
print('Você fechou o programa.')
