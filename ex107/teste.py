""" Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções."""

import moeda

valor = float(input('Digite um valor: '))
taxa_aumento = float(input('Digite uma taxa para aumento: '))
taxa_diminuir = float(input('Digite uma taxa para desconto: '))

print(f'O valor digitado foi: {valor}.')
print(f'O dobro do valor é {moeda.dobro(valor)}.')
print(f'A metade do valor é {moeda.metade(valor)}')
print(f'O triplo do valor é {moeda.triplo(valor)}.')
print(f'O valor com {taxa_aumento}% de aumento é {moeda.aumentar(valor, taxa_aumento)}')
print(f'O valor com {taxa_diminuir}% de desconto é {moeda.diminuir(valor, taxa_diminuir)}')
