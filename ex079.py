""" Crie um programa que o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados em ordem crescente."""

lista = []
resposta = 'S'
while True:
    if resposta == 'S':
        num = int(input('Digite um valor: '))
        while num in lista:
            print('Valor já se encontra na lista. Por favor, digite outro.')
            num = int(input('Digite um valor: '))
        lista.append(num)
        print('Valor adicionado com sucesso!')
        resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()
    else:
        break
print(f'A lista digitada foi {sorted(lista)}')


