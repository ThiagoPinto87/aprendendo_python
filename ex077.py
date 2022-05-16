""" Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais."""

# Captura as palavras que serão inseridas na tupla.
palavras = ('caderno', 'lapis', 'borracha', 'caneta', 'lapiseira', 'estojo', 'mochila')

# Laço de repetição para as palavras colocando cada palavra na variável "n"
for n in palavras:
    # Imprime o texto contendo cada palavra separadamente.
    print(f'\nNa palavra {n.upper()} temos as vogais ', end='')
    # Pega de cada palavra da variável n e destrincha em cada letra.
    for letra in n:
        # Coloca condicional perguntando se nas letras destrinchadas, há as vogais "AEIOU"
        # Observe que este for, está subordinado por indentação do "for" superior onde separa cada palavra da tupla.
        if letra.upper() in 'AEIOU':
            # Imprime as vogais que possuem em cada palavra.
            print(letra.upper(), end=' ')
