""" Crie um programa que vai ler vários números e colocar em uma lista.
Depois mostre:
a) Quantos números foram digitados.
b) A lista de valores ordenada de forma decrescente.
c) Se o valor 5 foi digitado e está ou não na lista."""
numero = []
while True:
    numero.append(int(input('Digite um número: ')))
    resp = input('Quer continuar? [S/N]: ').strip().upper()
    while resp not in 'SN':
        print('Informação inválida!')
        resp = input('Quer continuar? [S/N]: ').strip().upper()
    if resp == 'N':
        break
print('-=' * 20)
print(f'Foram digitados {len(numero)} números.')
numero.sort(reverse=True)
print(f'Os números digitados foram {numero}.')
if 5 in numero:
    print(f'O numero 5 foi digitado e está na posição {numero.index(5)+1}.')
else:
    print('O número 5 não foi digitado!')
