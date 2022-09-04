# Módulo de formulas exercício 109.

def dobro(num=0, formato=False):
    res = num * 2
    return res if formato is False else moeda(res)


def triplo(num=0, formato=False):
    res = num * 3
    return res if formato is False else moeda(res)


def aumentar(num=0, i=0, formato=False):
    res = num * (1 + i/100)
    return res if formato is False else moeda(res)


def diminuir(num=0, i=0, formato=False):
    res = num * (1 - i/100)
    return res if not formato else moeda(res)  # Forma diferente de escrever a string das demais porém, mesmo resultado.

def metade(num=0, formato=False):
    res = num / 2
    return res if formato is False else moeda(res)


def moeda(valor=0, form_moeda='R$'):
    """
    Formata no modo moeda em que usamos no Brasil.
    :param valor: Solicita valor a ser formatado.
    :param form_moeda: Solicita pra qual moeda quer fazer a formatação (Não faz calculo do câmbio).
    :return: Retorna o valor formatado.
    """
    return f'{form_moeda}{valor:>.2f}'.replace('.', ',')

