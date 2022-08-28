""" Crie um programa que tenha uma função chamada leiaint(), que vai funcionar de forma semelhante à função input() do
Python, só que fazendo a validação para aceitar apenas um valor numérico.
ex.:
n = leiaint('Digite um n') """


def leia_int(msg):
    ok = False
    valor = 0
    while True:
        resultado = str(input(msg))
        if msg.isnumeric():
            valor = int(resultado)
            ok = True
        else:
            print('\33[1:31mErro! Por favor, digite um número válido.\33[m')
        if ok:
            break
    return valor


# Programa principal.
n = leia_int('Digite um número: ')
print(f'Você digitou o número {n}.')
