"""Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atigiram a maioridade e quantas já são maiores.
Maioridade = 21 anos"""

# Importação de bibliotecas
from datetime import date

# Captura o ano atual do computador.
ano_atual = date.today().year

# Usa um aglutinador ou contador inicial de resultados.
cont_menor = 0
cont_maior = 0

# Faz o laço de sete resultados.
for pessoa in range(1, 8):
    # Solicita o input do ano a ser contado considerando a quantidade de for acima.
    ano_nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoa)))
    # Calcula a idade. Repare que o que permite que o calculo da idade seja possível é somente a IDENTAÇÃO,
    # Não tem vinculo algum com a pessoa dentro do laço for.
    idade = ano_atual - ano_nasc
    # Compara se é menor de 21 anos.
    if idade < 21:
        # Adiciona contagem ao cont_menor da linha 12.
        cont_menor += 1  # Essa expressão poderia ser escrita assim: cont_menor = cont_menor + 1
    else:
        # Adiciona contagem ao cont_maior da linha 13.
        cont_maior += 1
# Imprime o resultado do cont_menor.
print('Ao todo temos {} pessoas menores de idade.'.format(cont_menor))
# Imprime o resultado do cont_maior.
print('Por sua vez temos {} pessoas que são maiores de idade.'.format(cont_maior))