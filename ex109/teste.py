""" Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se
o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108."""

import moeda

valor = float(input('Digite um valor: '))
taxa_aumento = float(input('Digite uma taxa para aumento: '))
taxa_diminuir = float(input('Digite uma taxa para desconto: '))

print(f'O valor digitado foi: {moeda.moeda(valor)}.')
print(f'O dobro do valor é {moeda.dobro(valor, True)}.')
print(f'A metade do valor é {moeda.metade(valor, True)}')
print(f'O triplo do valor é {moeda.triplo(valor, True)}.')
print(f'O valor com {taxa_aumento}% de aumento é {moeda.aumentar(valor, taxa_aumento, True)}')
print(f'O valor com {taxa_diminuir}% de desconto é {moeda.diminuir(valor, taxa_diminuir, True)}')
