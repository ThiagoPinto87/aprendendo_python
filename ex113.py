""" Reescreva a função leiaint() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número
de tipo inválido.
Aproveite e crie também a função leiaFloat() com a mesma funcionalidade."""


def leia_int(msg):
    while True:
        try:
            resultado = int(input(msg))
        except Exception as erro:
            print('\33[1:31mErro! Por favor, digite um número válido.\33[m')
            print(f'\33[1:33mO erro refere-se a {erro.__class__}.\33[m')
        else:
            return resultado


def leia_float(msg):
    while True:
        try:
            resultado = float(input(msg))
        except Exception as erro:
            print('\33[1:31mErro! Por favor, digite um número válido.\33[m')
            print(f'\33[1:33mO erro refere-se a {erro.__class__}.\33[m')
        else:
            return resultado


# Programa principal.
n = leia_int('Digite um número Inteiro: ')
z = leia_float('Digite um número Real: ')
print(f'Você digitou o número inteiro {n} e o número real {z}.')
