"""Crie um programa que tenha um função chamada fatorial() que receba dois parâmetros: o primeiro que indique o número a
calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o
processo de calculo fatorial {colocar o docstring}"""


print('#' * 5, "FORMA DO PROFESSOR GUANABARA", '#' * 5)


def fatorial(n, show=False):
    """
       -> Calcula o fatorial de um número.
       :param n: Numero a ser fatorado.
       :param show: Imprime o calculo efetuado para o resultado.
       :return: O valor do número escolhido em "n".
       """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa Principal
print(fatorial(5, True))
#
#
#
#
# MINHA FORMA DE RESOLVER O PROBLEMA
print('#' * 13, "MINHA FORMA", '#' * 14)
"""Não consegui fazer com que no final do resultado mostrasse o símbolo de "=". """


def fatorial(n=1, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: Numero a ser fatorado.
    :param show: Imprime o calculo efetuado para o resultado.
    :return: O valor do número escolhido em "n".
    """
    f = 1
    if not show:
        for c in range(n, 0, -1):
            f *= c
        return f
    else:
        for c in range(n, 0, -1):
            print(f'{c} x ', end='')
            f *= c
        return f


# Programa Principal
print(fatorial(5, True))
