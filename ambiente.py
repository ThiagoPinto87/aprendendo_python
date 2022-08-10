# Interactive Help

help(range)

print(range.__doc__)

print('*' * 80)
# Docstrings


def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f' {c} ', end='')
        c += p
    print('FIM!')


help(contador)

contador(2, 10, 2)

print('*' * 80)
print('PARÂMETROS OPICIONAIS')


def somar(a, b, c=0):  # Neste caso o c por receber o valor padrão "0" ele se torna opcional para esta função.
    s = a + b + c
    print(f'A soma é {s}')


somar(5, 2, 3)
somar(5, 2)

print('*' * 80)
print('ESCOPO DE VARIÁVEIS')


def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
funcao()
print(f'N1 fora vale {n1}')
print()
print('-' * 15)

def teste(b):
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)
print('-' * 15)
print(f'A fora vale {a}')


print('*' * 80)
print('ESCOPO DE VARIÁVEIS COM FUNÇÃO GLOBAL')
def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)
print('-' * 15)
print(f'A fora vale {a}')

print('*' * 80)
print('RETORNO DE VALORES USANDO RETURN')

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(5, 2, 3)
r2 = somar(4, 8)
r3 = somar(9)

print(f'Os resultados das somas dos "r" é {r1}, {r2}, {r3}')
