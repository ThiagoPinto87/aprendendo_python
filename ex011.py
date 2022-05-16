#Calcule a área de uma parede e sabendo que cada litro de tinta pinta uma área de 2m², qual a quantidade de tinta tem que ser comprada.

#Captura as informações da parede.
largura = float(input('Digite a largura da parede:'))
altura = float(input('Digite a altura da parede:'))

#Calcula a área da parede.
area = largura * altura

#Calcula a quantidade de tinta com base no rendimento da tinta.
tinta = area / 2

#Imprime o relatório.
print('A sua parede tem uma área de {:.2f}m².\nCom isso, deve-se comprar {}L de tinta para pintá-la.'.format(area, tinta))
