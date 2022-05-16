""" Faça um programa que calcule a soma entre todos os números ímpares que são multiplos de três
e que se encontram no intervalor de 1 até 500."""

soma = 0
cont = 0
for contador in range(1, 501):
    if contador % 3 == 0 and contador % 2 != 0:
        soma += contador  # Neste caso ele soma pois inicialmente ele pega o valor da soma que é 0 (linha 4)
                          # e puxa o primeiro resultado do contador e adiciona à variável soma, e assim por diante.

        cont += 1         # Neste outro caso, ele pega o valor que tem de cont que é 0 (linha 5) e adiciona a cada
                          # resultado que ele encontra no laço "for".
        """O += quer dizer que está somando ele mesmo, ex.: cont = cont + 1"""
print('A soma dos {} resultados multiplos de 3 e ímpares é {}.'.format(cont, soma))
