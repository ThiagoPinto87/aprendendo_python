""" Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""

# Aglutinador de registro zerado e registros iniciais.
num = 0
cont = 1
controle = 'S'

# Captura o primeiro número.
num = int(input('Digite um número: '))

# Aglutinador de registros iniciais para maior e menor.
maior_num = num
menor_num = num

# Laço de controle de flag de parada.
while controle != 'N':
    # Solicita o outro número. Este número será controlado para verificar o maior, o menor e soma na formula do
    # problema.
    num_usuario = int(input('Digite outro número: '))
    # Formula do problema.
    num += num_usuario
    # Registra quando nas variáveis "maior_num" e "menor_num" os valores capturados em "num_usuario".
    if num_usuario > maior_num:
        maior_num = num_usuario
    elif num_usuario < menor_num:
        menor_num = num_usuario
    # Contador de registros.
    cont += 1
    # Controle de novos lançamentos colocando a letra digitada em maiúscula, retirando os espaços e considerando
    # somente a primeira letra
    controle = str(input('Quer continuar digitar números? [S / N]')).upper().strip()[0]
    # Controle quanto a dígitos errados de usuários.
    while controle != 'S' and controle != 'N':
        print('Informação inválida. Por favor, digite [S / N]')
        controle = str(input('Quer continuar digitar números? [S / N]')).upper()
# Imprime os relatórios.
print('Você digitou {} números. A média deles corresponde a: {:.2f}!'.format(cont, num/cont))
print('O maior número é {} e o menor é {}.'.format(maior_num, menor_num))
