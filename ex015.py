# Calcule o aluguel de um carro levando em consideração que a diária custa R$60,00 e o preço do Km rodado é de R$0,15.

# Captura a informação de quantidade de diárias.

diaria = int(input('Quantos dias será alugado?'))

# Calcula o valor total de diárias.

vlrdiarias = diaria * 60

# Captura a quantidade de Km rodado.

kmrodado = float(input('Qual a quantidade de km rodados?'))

# Calcula o valor total de Km rodado.

vlrrodado = kmrodado * 0.15

# Calcula o valor total a pagar.

vlrapagar = vlrrodado + vlrdiarias

# Imprime o relatório.

print('Você alugou o carro por {} dias e rodou a quantidade de {}km.'.format(diaria, kmrodado))
print('O valor de diárias é R${:.2f} e de Km rodado é R${:.2f}.'.format(vlrdiarias, vlrrodado))
print('O valor total a pagar é R${:.2f}'.format(vlrapagar))


