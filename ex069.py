""" Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No vinal, mostre:
a) Quantas pessoas tem mais de 18 anos.
b) Quantos homens foram cadastrados.
c) Quantas mulheres tem menos de 20 anos."""

# ERRADO!!!!
# Falta tratar entrada de dados erradas como F OU M digitados errado.


# Margem de decoração e título.
print('-=' * 20)
print(' ' * 10, 'CADASTRO DE PESSOAS', ' ' * 10)
print('-=' * 20)

# Aglutinadores de contagens zerados.
cont_homens = 0
cont_mulheres20 = 0
cont_18anos = 0

# Primeira captura de valores.
sexo = str(input('Digite se [M/F]: ')).strip().upper()
idade = int(input('Digite a idade: '))
# Verificação das condições para impressão do relatório.
if sexo == 'M':
    cont_homens += 1
elif sexo != 'F':
    sexo = str(input('Digite se [M/F]: ')).strip().upper()
if idade >= 18:
    cont_18anos += 1
if sexo == 'F' and idade < 20:
    cont_mulheres20 += 1
# Laço de repetição para continuar a digitar.
while True:
    continuar = str(input('Deseja lançar mais? [S/N]')).strip().upper()
    if continuar == 'S':
        print('-' * 40)
        # Captura de valores.
        sexo = str(input('Digite se [M/F]: ')).strip().upper()
        idade = int(input('Digite a idade: '))
        # Verificação das condições para impressão do relatório.
        if sexo == 'M':
            cont_homens += 1
        if idade >= 18:
            cont_18anos += 1
        if sexo == 'F' and idade < 20:
            cont_mulheres20 += 1
    # Flag de parada do laço True.
    else:
        # Margens de decoração.
        print('-=' * 20)
        print('RELATÓRIO DE FIM DO PROGRAMA')
        print('-=' * 20)
        # Flag de parada de laço True.
        break
# Relatórios.
print('Foram lançados:')
print(f'- {cont_18anos} pessoas que possuem + 18 Anos.')
print(f'- {cont_homens} homens.')
print(f'- {cont_mulheres20} mulheres com menos de 20 anos.')