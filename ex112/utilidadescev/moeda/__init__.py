# Módulo de formulas exercício 111.

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


def moeda_resumo(valor, aum, desc):
    print('-' * 25)
    print('     RESUMO DE VALOR')
    print('-' * 25)
    print('DESCRIÇÃO        VALOR')
    print(f'Metade \t\t\t{metade(valor, True)}')  # A "\t" é utilizado para tabulação.
    print(f'Dobro \t\t\t{dobro(valor, True)}')  # A "\t" é utilizado para tabulação.
    print(f'Triplo \t\t\t{triplo(valor, True)}')  # A "\t" é utilizado para tabulação.
    print(f'Aumentar {aum}%\t{aumentar(valor, aum,True)}')  # A "\t" é utilizado para tabulação.
    print(f'Diminuir {desc}%\t{diminuir(valor, desc, True)}')  # A "\t" é utilizado para tabulação.
    print('-' * 25)

