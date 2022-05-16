""" Crie um programa que leia  vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag de parada)."""

# Aglutinador de variáveis zeradas.
num = 0
num1 = 0
cont = 0

# Laço de repetição com flag de parada.
while num1 != 999:
    # Solicita o número a ser somado.
    num1 = int(input('Digite um número: '))
    # Controla se o Flag de parada deve ser acionado.
    if num1 != 999:
        # Formula do problema.
        num += num1  # Essa string quer dizer: "num = num + num1"
        # Contador de registros.
        cont +=1
# Imprime o relatório.
print('A soma dos {} números digitados é {}.'.format(cont, num))
