""" Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequencia.
No final, mostre uma listagem de preços, organizando os dados em forma tabular."""

# Captura das informações para a tupla (lembrando que a tupla pode conter qualquer típo de elemento String e inteiros por exemplo:
lista_produtos = ('caneta', 1, 'lapis', 0.75, 'borracha', 0.5, 'caderno', 15, 'grampeador', 8.90, 'lapiseira', 1.5)

# Margem decorativa.
print('-=' * 20)
print(f'{"PAPELARIA THIAGO":^40}')  # Título com 40 caracteres centralizado.
print('-=' * 20)
# Laço de repetição com controle de posição e considerando o tamanho da lista_produtos para concluir.
for pos in range(0, len(lista_produtos)):
    # Verificação condicional quanto ao índice de cada posição "pos" colocando os pares à esquerda (produtos).
    if pos % 2 == 0:  # Pares.
        print(f'{lista_produtos[pos]:.<30}'.upper(), end='')  # Produtos com 30 caracteres alinhados à esquerda com pontos.
    # Verificação condicional quanto ao índice de cada posição "pos" colocando os ímpares à direita (Valdor produtos).
    else:  # Ímpares.
        print(f'R${lista_produtos[pos]:>8.2f}')  # Valores com 8 caracteres alinhados à direita e com duas casas decimais.
# Margem decorativa.
print('-=' * 20)
