""" Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No vinal, mostre:
a) Quantas pessoas tem mais de 18 anos.
b) Quantos homens foram cadastrados.
c) Quantas mulheres tem menos de 20 anos."""

cont_idade_18 = cont_sexo = cont_mulher_20 = 0

print('-=' * 25)
print(' ' * 15, 'CADASTRO DE PESSOAS', ' ' * 15)
print('-=' * 25)
while True:
    idade = int(input('Qual a idade: '))
    sexo = str(input('Qual o sexo: ')).upper().strip()[0]
    while sexo not in 'FM':
        sexo = str(input('Qual o sexo: ')).upper().strip()[0]
    resposta = str(input('Quer continuar a lançar? [S/N]: ')).upper().strip()[0]
    while resposta not in 'SN':
        resposta = str(input('Quer continuar a lançar? [S/N]: ')).upper().strip()[0]
    if idade > 18:
        cont_idade_18 += 1
    if sexo == 'M':
        cont_sexo += 1
    if sexo == 'F' and idade < 20:
        cont_mulher_20 += 1
    if resposta == 'N':
        break
print('=-' * 25)
print(f'Foram registradas {cont_idade_18} com mais de 18 Anos.')
print(f'Foram cadastrados {cont_sexo} homens.')
print(f'Foram cadastradas {cont_mulher_20} mulheres com menos de 20 anos.')
