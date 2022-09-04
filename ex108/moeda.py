# Módulo de formulas exercício 108.

def dobro(num=0):
    res = num * 2
    return res


def triplo(num=0):
    res = num * 3
    return res


def aumentar(num=0, i=0):
    res = num * (1 + i/100)
    return res


def diminuir(num=0, i=0):
    res = num * (1 - i/100)
    return res

def metade(num=0):
    res = num / 2
    return res


def moeda(valor, form_moeda='R$'):
    return f'{form_moeda}{valor:>.2f}'.replace('.', ',')  # Próximo desafio é colocar com separador de milhar com if's.
