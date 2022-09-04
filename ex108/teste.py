""" Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como
um valor monetário formatado."""

from ex108 import moeda

valor = float(input('Digite um valor: '))
taxa_aumento = float(input('Digite uma taxa para aumento: '))
taxa_diminuir = float(input('Digite uma taxa para desconto: '))

print(f'O valor digitado foi {moeda.moeda(valor)}')
print(f'O dobro do valor é {moeda.moeda(moeda.dobro(valor))}.')
print(f'A metade do valor é {moeda.moeda(moeda.metade(valor))}')
print(f'O triplo do valor é {moeda.moeda(moeda.triplo(valor))}.')
print(f'O valor com {taxa_aumento:.2f}% de aumento é {moeda.moeda(moeda.aumentar(valor, taxa_aumento))}')
print(f'O valor com {taxa_diminuir:.2f}% de desconto é {moeda.moeda(moeda.diminuir(valor, taxa_diminuir))}')
