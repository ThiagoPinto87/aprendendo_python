"""Crie um programa que tem uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições."""


def voto(ano):
    """
    Indica através do parâmetro ano (int) referente ao ano de nascimento, se o voto é NEGADO, OPCIONAL ou OBRIGATÓRIO.
    :param ano: Ano de nascimento.
    :return: Sem parâmetro
    """
    from datetime import date
    resp = date.today().year - ano
    if resp < 0:
        return f'O ano de {ano} é maior que o ano atual ({date.today().year}). Por favor, re-veja sua resposta.'
    elif resp < 16:
        return f'Com {resp} anos o NÃO VOTA!'
    elif 16 <= resp < 65:
        return f'Com {resp} anos o voto é OBRIGATÓRIO!'
    elif 65 < resp < 110:
        return f'Com {resp} anos o voto é OPCIONAL.'
    elif resp > 110:
        return f'Com {resp} anos o voto é OPCIONAL. Porém, re-veja se a informação está correta!'


# Programa principal
print(voto(int(input('Em que ano você nasceu? '))))
